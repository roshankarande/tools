from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
   wait_time = between(5, 15)
    
   @task(2)
   def homepage(self):
      self.client.get("/")
        
   @task(1)
   def about_page(self):
      self.client.get("/about/")