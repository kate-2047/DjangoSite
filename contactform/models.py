from django.db import models

# Create your models here.

# data from contact form to database
class ContactSubmission(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"