from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model= Project
    fields = ('project_title', 'screenshot', 'project_description', 'live_link', 'date_posted', 'user')
    
