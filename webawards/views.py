from django.shortcuts import render
from django.http import Http404

from .models import Project

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

def search_projects(request):
  if 'search' in request.GET and request.GET['search']:
    title_search = request.GET.get('search')
    searched_projects = Project.search_by_title(title_search)
    message = f"{title_search}"
    return render(request, 'search-results.html', {"message":message, "projects":searched_projects})
  else:
    message = "You have not yer made a search"
    return render(request, 'search-results.html', {"message":message})
