from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import EmailForm

# Create your views here.

def send_email_view(request):
    form = EmailForm(request.POST or None)
    sent = False

    # clean form data
    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        full_message = f"Message from {name} <{email}>: \n\n{message}"

        # form the message and send
        send_mail(
            subject="New Email from Towne Engineering Website",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],
        )

        sent = True

    return render(request, 'emailservice/email_form.html', {'form':form, 'sent':sent})