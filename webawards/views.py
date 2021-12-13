from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Project, Votes, Profile
from .forms import ProfileForm, RatingForm, ProjectForm
from .serializer import ProfileSerializer, ProjectSerializer

# Create your views here.
def home(request):
  projects=Project.get_all_projects()
  return render(request, 'index.html', {"projects":projects})

@login_required(login_url='/accounts/login/')
def project_details(request, project_id):
  form = RatingForm(request.POST)
  try:
    project_details = Project.objects.get(pk = project_id)
    project_votes = Votes.objects.filter(project__id=project_id).all()
  except Project.DoesNotExist:
    raise Http404
  
  return render(request, 'ProjectDetails.html', {"details":project_details, "votes":project_votes, "form":form})

@login_required(login_url='/accounts/login/')
def profile(request):
  current_user=request.user.id
  profile = Profile.objects.filter(user__id = current_user)
  return render(request, 'profile.html', {"profile":profile})

def create_profile(request):
  # if request.method=="POST":
  #   try:
  #     profile = Profile.objects.get(profile_id=request.profile.id)
  #     form = ProfileForm(request.POST, request.FILES, instance=profile)
  #     form.save()
      
  #     messages.success(request, 'Your profile has been updated successfully')
  #     return redirect('profile')
    
  #   except Profile.DoesNotExist:
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      profile_photo = form.save(commit=False)
      user_bio = form.cleaned_data.get('user_bio')
      form.instance.user = request.user
      
      form.save()
      
      messages.success(request, 'Your profile has been created successfully')
      return redirect('profile')
    else:
      form = ProfileForm()
      
    return render(request, 'createprofile.html', {"form":form})
        
    

def search_projects(request):
  if 'search' in request.GET and request.GET['search']:
    title_search = request.GET.get('search')
    searched_projects = Project.search_by_title(title_search)
    message = f"{title_search}"
    return render(request, 'search-results.html', {"message":message, "projects":searched_projects})
  else:
    message = "You have not yer made a search"
    return render(request, 'search-results.html', {"message":message})

@login_required(login_url='/accounts/login/')
def submit_rating(request, project_id):
  url = request.META.get('HTTP_REFERER')
  if request.method == 'POST':
    try:
      rating = Votes.objects.get(user__id=request.user.id, project__id=project_id)
      form = RatingForm(request.POST, instance=rating)
      form.save()
      messages.success(request, 'Your rating has been updated')
      return redirect(url)
    except Votes.DoesNotExist:
      form = RatingForm(request.POST)
      if form.is_valid():
        # rating_data = Votes()
        design_score = form.cleaned_data.get('design_score')
        usability_score = form.cleaned_data.get('usability_score')
        content_score = form.cleaned_data.get('content_score')
        # form.instance.Avg_score = design_score
        form.instance.project_id=project_id
        form.instance.user_id = request.user.id
        form.save()
        messages.success(request, 'Your rating has been posted')
        
        return redirect(url)

@login_required(login_url='/accounts/login/')      
def post_project(request):
  
  if request.method=="POST":
    form= ProjectForm(request.POST, request.FILES)
    if form.is_valid():
      project_title = form.cleaned_data.get('project_title')
      screenshot = form.save(commit=False)
      project_description = form.cleaned_data.get('project_description')
      live_link = form.cleaned_data.get('live_link')
      form.instance.user = request.user
      
      form.save()
      return redirect('home')
  else:
    form = ProjectForm()
    
  return render(request, "newproject.html", {"form":form})

class ProjectList(APIView):
  def get(self, request, format=None):
    all_projects = Project.objects.all()
    serializers=ProjectSerializer(all_projects, many=True)
    return Response(serializers.data)
  
class ProfileList(APIView):
  def get(self, request, format=None):
    all_profiles = Profile.objects.all()
    serializers = ProfileSerializer(all_profiles, many=True)
    return Response(serializers.data)
    