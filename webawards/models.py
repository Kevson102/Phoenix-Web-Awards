from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  profile_photo = models.ImageField(upload_to='static/images/')
  user_bio = models.TextField()
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  
  def save_profile(self):
    self.save()
    
  def delete_profile(self):
    self.delete()
  
  def __str__(self):
    return self.user_bio
  
class Project(models.Model):
  project_title = models.CharField(max_length=40)
  screenshot = models.ImageField(upload_to='static/images/')
  project_description = models.TextField()
  live_link = models.URLField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def save_project(self):
    self.save()
  
  def __str__(self):
    return self.project_title