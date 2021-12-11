from django.test import TestCase
from .models import Profile, User, Project

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
      
      
class ProjectTestCase(TestCase):
  # set up method
  def setUp(self):
    user, created = User.objects.get_or_create(username = 'kevson', email='kevson102@gmail.com', password ='password')
    
    # Create a profile instance and save it
    self.profile = Profile(profile_photo='profile.picture', user_bio ='This is my biography info', user= user)
    self.profile.save_profile()
    
    # Create a test project
    self.project = Project(project_title='portfolio', screenshot='portfolio.image.png', project_description='This is my professional portfolio', live_link='https://kevson.com/portfolio', user = user)
    self.project.save()
    
  # Test instance
  def test_instance(self):
    self.assertTrue(isinstance(self.project, Project))
    
  # Test save project method
  def test_save_project(self):
    self.project.save_project()
    saved_projects = Project.objects.all()
    self.assertTrue(len(saved_projects)==1)
  
  # Test delete project
  def test_delete_project(self):
    self.project.save_project()
    self.project.delete_project()
    saved_projects = Project.objects.all()
    self.assertTrue(len(saved_projects)==0)
    
  # Test get all projects
  def test_get_all_projects(self):
    user, created = User.objects.get_or_create(username = 'kevson102', email='kevson226@gmail.com', password ='password2')

    self.project.save_project()
    self.project2 = Project(project_title='migrators', screenshot='migrators.image.png', project_description='This is my migration website', live_link='https://kevson102.com/portfolio', user = user)
    self.project2.save_project()
    saved_projects = Project.get_all_projects()
    self.assertTrue(len(saved_projects)==2)
    