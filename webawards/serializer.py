from rest_framework import serializers
from .models import Profile, Project

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model= Project
    fields = ('project_title', 'screenshot', 'project_description', 'live_link', 'date_posted', 'user')
    
class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ('profile_photo', 'user_bio', 'user')
    
