from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Story, Project, Event,Banner
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from rest_framework import viewsets
from .serializers import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    user = request.user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'account/login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def index(request):
    stories = Story.objects.all()
    projects = Project.objects.all()
    events = Event.objects.all()
    return render(request, 'events/index.html', {'stories': stories, 'projects': projects, 'events': events})

def story_list(request):
    stories = Story.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(stories, 5) 

    try:
        stories = paginator.page(page)
    except PageNotAnInteger:
        stories = paginator.page(1)
    except EmptyPage:
        stories = paginator.page(paginator.num_pages)
    return render(request, 'events/story_list.html', {'stories': stories})

def project_list(request):
    projects = Project.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(projects, 5) 

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    return render(request, 'events/project_list.html', {'projects': projects})

def event_list(request):
    events = Event.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(events, 5) 

    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    return render(request, 'events/event_list.html', {'events': events})

def story_table(request):
    return render(request,'table-basic.html')

def banner_footer_list(request):
    banners = Banner.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(banners, 5) 

    try:
        banners = paginator.page(page)
    except PageNotAnInteger:
        banners = paginator.page(1)
    except EmptyPage:
        banners = paginator.page(paginator.num_pages)
    return render(request,'events/settings.html', {'banners':banners})




# banner/footer-view

def banner_add(request):
    if request.method == 'POST':
        banner_image = request.FILES.get('banner_image')
        title = request.POST.get('title')
        description = request.POST.get('description')
        address = request.POST.get('address')
        Banner.objects.create(
            banner_image=banner_image,
            title=title,
            description=description,
            address=address
        )
        return redirect('index')
    return render(request,'events/add_settings.html')


def banner_delete(request,pk):
    banner = get_object_or_404(Banner, pk=pk)
    
    if request.method == 'POST':
        banner.delete()
        return redirect('index')
    return render(request,'events/delete_banner.html',{'banner':banner})


def banner_edit(request,pk):
    banner = get_object_or_404(Banner, pk=pk)
    
    if request.method == 'POST':
        banner_image = request.FILES.get('banner_image')
        title = request.POST.get('title')
        description = request.POST.get('description')
        address = request.POST.get('address')
        
        banner.banner_image = banner_image
        banner.title = title
        banner.description = description
        banner.address = address
        banner.save()
        return redirect('index')
    return render(request, 'events/edit_banner.html',{'banner':banner})



# story-view

def story_add(request):
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        title = request.POST.get('title')
        date = request.POST.get('date')
        Story.objects.create(
            photo=photo, 
            title=title, 
            date=date
        )
        return redirect('index')
    return render(request,'events/add_story.html')


def story_delete(request, pk):
    story = get_object_or_404(Story, pk=pk)

    if request.method == 'POST':
        story.delete()
        return redirect('index')
    return render(request, 'events/delete_story.html', {'story': story})


def story_edit(request, pk):
    story = get_object_or_404(Story, pk=pk)

    if request.method == 'POST':
        photo = request.FILES.get('photo')
        title = request.POST.get('title')
        date = request.POST.get('date')

        story.photo = photo
        story.title = title
        story.date = date
        story.save()

        return redirect('index')

    return render(request, 'events/edit_story.html', {'story': story})

# project-view



def project_add(request):
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        title = request.POST.get('title')
        date = request.POST.get('date')
        Project.objects.create(
            photo=photo, 
            title=title, 
            date=date
        )
        return redirect('index')
    return render(request,'events/add_project.html')


def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('index')

    return render(request, 'events/delete_project.html', {'project': project})


def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        photo = request.FILES.get('photo')
        title = request.POST.get('title')
        date = request.POST.get('date')

        project.photo = photo
        project.title = title
        project.date = date
        project.save()
        return redirect('index')

    return render(request, 'events/edit_project.html', {'project': project})


# event-view

def event_add(request):
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        title = request.POST.get('title')
        description = request.POST.get('description')
        Event.objects.create(
            photo=photo, 
            title=title, 
            description=description
        )
        return redirect('index')
    return render(request,'events/add_event.html')


def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method == 'POST':
        event.delete()
        return redirect('index')

    return render(request, 'events/delete_event.html', {'event': event})


def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)

    if request.method == 'POST':
        photo = request.FILES.get('photo')
        title = request.POST.get('title')
        description = request.POST.get('description')

        event.photo = photo
        event.title = title
        event.description = description
        event.save()
        return redirect('index')

    return render(request, 'events/edit_event.html', {'event': event})


# banner/fotter-edit


# ------------------------------------
class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer