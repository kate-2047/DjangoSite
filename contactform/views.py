from django.shortcuts import render
from .forms import ContactForm
from .models import ContactSubmission

# Create your views here.

def contact_view(request):
    submitted = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            # save input to text file as backup
            with open('contact_submissions.txt', 'a') as file:
                file.write(f"Name: {name}, Email: {email}\n\n")
            
            # save to database
            ContactSubmission.objects.create(name=name, email=email)

            submitted = True

    else:
        form = ContactForm()

    return render(request, 'contactform/contact.html', {'form': form, 'submitted': submitted})