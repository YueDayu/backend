"""
WSGI config for DressSite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import sys

path = "/data/www/DressSite"
if not path in sys.path:
	sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DressSite.settings")

application = get_wsgi_application()
