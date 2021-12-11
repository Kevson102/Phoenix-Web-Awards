from django.test import TestCase
from .models import Profile, User

# Create your tests here.
class ProfileTestCase(TestCase):
  # set up method
  def setUp(self):
    user, created = User.objects.get_or_create(username = 'kevson', email='kevson102@gmail.com', password ='password')
    self.profile = Profile(profile_photo='profile.picture', user_bio ='This is my biography info', user= user)
    
  # Test Instance
  def test_instance(self):
    self.assertTrue(isinstance(self.profile, Profile))
    
  # Test save profile
  def test_save_profile(self):
    self.profile.save_profile()
    profiles = Profile.objects.all()
    self.assertTrue(len(profiles)==1)
    
  def test_delete_profile(self):
    self.profile.save_profile()
    self.profile.delete_profile()
    profiles = Profile.objects.all()
    self.assertTrue(len(profiles)==0)
      