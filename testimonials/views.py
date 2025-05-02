from django.shortcuts import render
from .forms import TestimonialForm
from .models import Testimonial

# Create your views here.

def testimonial_view(request):
    submitted = False

    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else: 
        form = TestimonialForm

    return render(request, 'testimonials/testimonial.html', {'form':form, 'submitted':submitted})

def testimonial_list(request):
    testimonials = Testimonial.objects.order_by('-created_at')
    return render(request, 'testimonials/testimonial_list.html', {'testimonials': testimonials})

