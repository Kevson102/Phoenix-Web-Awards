from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  profile_photo = models.ImageField(upload_to='static/images/')
  user_bio = models.TextField()
  email = models.EmailField()
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.user_bio