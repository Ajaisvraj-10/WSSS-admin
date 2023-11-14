from django.contrib import admin
from .models import Story, Project, Event,Banner

# Register your models here.

admin.site.register(Story)
admin.site.register(Project)
admin.site.register(Event)
admin.site.register(Banner)