from django import forms
from .models import Profile, Votes,Project

class RatingForm(forms.ModelForm):
  class Meta:
    model = Votes
    fields = ['design_score', 'usability_score', 'content_score']
    
class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['project_title', 'screenshot', 'project_description', 'live_link']
    
class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['profile_photo', 'user_bio']
    
