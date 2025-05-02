from django.urls import path
from .views import testimonial_view, testimonial_list

urlpatterns = [
    path('', testimonial_view, name='testimonial'),
    path('all/', testimonial_list, name='testimonial_list')
]
