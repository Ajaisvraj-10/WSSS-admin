from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import *


router = DefaultRouter()
router.register(r'story',StoryViewSet)
router.register(r'project',ProjectViewSet)
router.register(r'event',EventViewSet)
router.register(r'banner',BannerViewSet)



urlpatterns = [
    path('api/admin', include(router.urls)),

    path('stories/', story_list, name='story_list'),
    path('story/add/', story_add, name='add_story'),
    path('story/<int:pk>/delete/', story_delete, name='story_delete'),
    path('story/<int:pk>/edit/', story_edit, name='story_edit'),
    path('story_table', story_table, name='story_table'),
    
    
    path('projects/', project_list, name='project_list'),
    path('project/add/', project_add, name='add_project'),
    path('project/<int:pk>/delete/', project_delete, name='project_delete'),
    path('project/<int:pk>/edit/', project_edit, name='project_edit'),
    
    
    path('events/', event_list, name='event_list'),
    path('event/add/', event_add, name='add_event'),
    path('event/<int:pk>/delete/', event_delete, name='event_delete'),
    path('event/<int:pk>/edit/',event_edit, name='event_edit'),
    
    
    path('settings/', banner_footer_list, name='banner_footer_list'),    
    path('settings/add/', banner_add, name='add_banner'),    
    path('settings/<int:pk>/delete/', banner_delete, name='banner_delete'),
    path('settings/<int:pk>/edit/', banner_edit, name='banner_edit'),

    
    path('', index, name='index'),
    path('login/', login_view, name='admin_login'),     
    path('logout/', logout_view, name='admin_logout'),

]