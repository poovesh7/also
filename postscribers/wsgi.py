"""
WSGI config for postscribers project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project's base directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the default settings module for the 'django' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'postscribers.settings')

# Get the WSGI application
application = get_wsgi_application()
