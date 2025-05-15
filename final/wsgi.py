"""
WSGI config for final project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
# Import
import os
from django.core.wsgi import get_wsgi_application

# Settings module for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final.settings')

# Additional Changes


# Load WSGI
application = get_wsgi_application()
