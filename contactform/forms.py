from django import forms
 # contact form, can leave name and email to be stored in a designated file

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()