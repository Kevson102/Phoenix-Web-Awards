from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'index.html')

def project_details(request):
  return render(request, 'ProjectDetails.html')

def profile(request):
  return render(request, 'profile.html')
