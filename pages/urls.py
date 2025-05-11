from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contactus/', views.contactus, name='contactus'),
    path('contactform/', views.contactus, name='contact_form'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)