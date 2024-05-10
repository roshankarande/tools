from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
   wait_time = between(5, 15)
    
   @task
   def homepage(self):
      self.client.get("/")
    # self.client.get("/", headers={}, params={})