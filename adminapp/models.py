from django.db import models

# Create your models here.

class Story(models.Model):
    photo = models.ImageField(upload_to='story_photos/')
    title = models.CharField(max_length=100)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
    photo = models.ImageField(upload_to='project_photos/')
    title = models.CharField(max_length=100)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    photo = models.ImageField(upload_to='event_photos/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
class Banner(models.Model):
    banner_image = models.ImageField(upload_to='banner_photos/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    address =  models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
