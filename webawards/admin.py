from django.contrib import admin

from webawards.models import Profile, Project, Votes

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Votes)