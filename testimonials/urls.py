from django.urls import path
from .views import testimonial_view, testimonial_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', testimonial_view, name='testimonial'),
    path('all/', testimonial_list, name='testimonial_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
