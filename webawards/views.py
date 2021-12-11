from django.shortcuts import render

from webawards.models import Project

# Create your views here.
def home(request):
  projects=Project.get_all_projects()
  return render(request, 'index.html', {"projects":projects})

def project_details(request):
  return render(request, 'ProjectDetails.html')

def profile(request):
  return render(request, 'profile.html')
