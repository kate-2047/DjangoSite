from django.db import models


# About page
class AboutCo(models.Model):
    paragraph = models.TextField()

    def __str__(self):
        return self.paragraph[:50] + "..." # preview in admin

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.role}"
    

# Project page
class ProjectIntro(models.Model):
    paragraph = models.TextField()

    def __str__(self):
        return self.paragraph[:50] + "..." # preview in admin
    
class Project(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField()
    photo = models.ImageField(upload_to='image/', null=True, blank=True)

    def __str__(self):
        return self.name