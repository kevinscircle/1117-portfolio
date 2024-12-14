from django.contrib import admin
from .models import Skill, Project, Experience


# Register your models here.

admin.site.register(Skill)
admin.site.register(Project)  # Register the Project model
admin.site.register(Experience)  # Register the Experience model
