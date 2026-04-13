# locustfile.py
from locust import HttpUser, task, between

class QuickStartUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://httpbin.org"

    @task
    def hello_world(self):
        self.client.get("/get")

    @task(3)
    def view_items(self):
        self.client.get("/headers")