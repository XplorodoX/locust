from locust.util.exception_handler import retry
from locust.util.rounding import proper_round
from locust.util.timespan import parse_timespan

import unittest
from unittest.mock import patch


class TestParseTimespan(unittest.TestCase):
    def test_parse_timespan_invalid_values(self):
        self.assertRaises(ValueError, parse_timespan, None)
        self.assertRaises(ValueError, parse_timespan, "")
        self.assertRaises(ValueError, parse_timespan, "q")

    def test_parse_timespan(self):
        self.assertEqual(7, parse_timespan("7"))
        self.assertEqual(7, parse_timespan("7s"))
        self.assertEqual(60, parse_timespan("1m"))
        self.assertEqual(7200, parse_timespan("2h"))
        self.assertEqual(3787, parse_timespan("1h3m7s"))


class TestRounding(unittest.TestCase):
    def test_rounding_down(self):
        self.assertEqual(1, proper_round(1.499999999))
        self.assertEqual(5, proper_round(5.499999999))
        self.assertEqual(2, proper_round(2.05))
        self.assertEqual(3, proper_round(3.05))

    def test_rounding_up(self):
        self.assertEqual(2, proper_round(1.5))
        self.assertEqual(3, proper_round(2.5))
        self.assertEqual(4, proper_round(3.5))
        self.assertEqual(5, proper_round(4.5))
        self.assertEqual(6, proper_round(5.5))


class TestExceptionHandler(unittest.TestCase):
    def test_retry_returns_without_exception(self):
        @retry(delays=(1,))
        def f():
            return "ok"

        self.assertEqual("ok", f())

    def test_retry_then_success(self):
        state = {"calls": 0}

        @retry(delays=(7,), exception=ValueError)
        def f():
            state["calls"] += 1
            if state["calls"] == 1:
                raise ValueError("first failure")
            return "ok"

        with patch("locust.util.exception_handler.time.sleep") as sleep_mock:
            result = f()

        self.assertEqual("ok", result)
        self.assertEqual(2, state["calls"])
        sleep_mock.assert_called_once_with(7)

    def test_retry_exhausted_raises(self):
        @retry(delays=(1, 2), exception=ValueError)
        def f():
            raise ValueError("always failing")

        with patch("locust.util.exception_handler.time.sleep") as sleep_mock:
            with self.assertRaises(ValueError):
                f()

        self.assertEqual([1, 2], [call.args[0] for call in sleep_mock.call_args_list])

    def test_retry_does_not_catch_other_exception_types(self):
        @retry(delays=(1, 2), exception=ValueError)
        def f():
            raise TypeError("wrong type")

        with patch("locust.util.exception_handler.time.sleep") as sleep_mock:
            with self.assertRaises(TypeError):
                f()

        sleep_mock.assert_not_called()
