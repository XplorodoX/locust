import logging
import time

logger = logging.getLogger(__name__)


def retry(delays=(1, 3, 5), exception=Exception):
    def decorator(function):
        def wrapper(*args, **kwargs):
            cnt = 0
            for delay in delays:
                try:
                    return function(*args, **kwargs)
                except exception as e:
                    cnt += 1
                    logger.info("Exception found on retry %d: -- retry after %ds" % (cnt, delay))
                    logger.exception(e)
                    time.sleep(delay)

            try:
                return function(*args, **kwargs)
            except exception:
                logger.info("Retry failed after %d times." % (cnt))
                raise

        return wrapper

    return decorator
