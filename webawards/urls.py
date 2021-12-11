from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^detailed-Project/', views.project_details),
    url(r'^accounts/profile/', views.profile, name='profile'),
    url(r'^details/(?P<project_id>\d+)', views.project_details, name='project_details'),
]
