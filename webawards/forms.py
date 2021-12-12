from django import forms
from .models import Votes,Project

class RatingForm(forms.ModelForm):
  class Meta:
    model = Votes
    fields = ['design_score', 'usability_score', 'content_score']
    
class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['project_title', 'screenshot', 'project_description', 'live_link']
    
    