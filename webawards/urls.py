from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^detailed-Project/', views.project_details),
    url(r'^accounts/profile/', views.profile, name='profile'),
    url(r'^details/(?P<project_id>\d+)', views.project_details, name='project_details'),
    url(r'search/', views.search_projects, name='search_projects'),
    url(r'^submit_rating/(?P<project_id>\d+)', views.submit_rating, name='submit_rating'),
    url(r'^new/project/', views.post_project, name='post_project'),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^api/Profiles/$', views.ProfileList.as_view()),

]
