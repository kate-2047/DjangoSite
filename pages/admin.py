from django.contrib import admin
from .models import ProjectIntro, Project, TeamMember, AboutCo

# Register your models here.

# example user login
# username: example
# password: testing987

admin.site.register(Project)
admin.site.register(ProjectIntro)
admin.site.register(TeamMember)
admin.site.register(AboutCo)