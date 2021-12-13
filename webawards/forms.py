from django import forms
from .models import Profile, Votes,Project

class RatingForm(forms.ModelForm):
  class Meta:
    model = Votes
    fields = ['design_score', 'usability_score', 'content_score']
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # your calculate
        instance.Avg_score = instance.design_score + instance.usability_score
        if commit:
            instance.save()
        return instance
    
class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['project_title', 'screenshot', 'project_description', 'live_link']
    
class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['profile_photo', 'user_bio']
    
