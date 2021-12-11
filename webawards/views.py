from django.shortcuts import render
from django.http import Http404

from webawards.models import Project

# Create your views here.
def home(request):
  projects=Project.get_all_projects()
  return render(request, 'index.html', {"projects":projects})

def project_details(request, project_id):
  try:
    project_details = Project.objects.get(pk = project_id)
  except DoesNotExist:
    raise Http404
  
  return render(request, 'ProjectDetails.html', {"details":project_details})

def profile(request):
  return render(request, 'profile.html')
