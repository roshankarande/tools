from locust import HttpUser, task, between, SequentialTaskSet

class UserBehavior(SequentialTaskSet):
    
   @task
   def homepage(self):
      self.client.get("/")
        
   @task
   def about_page(self):
      self.client.get("/about/")

class WebsiteUser(HttpUser):
   tasks = [UserBehavior]
   wait_time = between(5, 15)