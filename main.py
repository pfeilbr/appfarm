import sys
from google.appengine.ext.webapp import util

# Uninstall Django 0.96.
for k in [k for k in sys.modules if k.startswith('django')]:
  del sys.modules[k]

# Add Django 1.0 archive to the path.
django_path = 'django.zip'
sys.path.insert(0, django_path)

# Django imports and other code go here...
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django.core.handlers.wsgi

def main():
  # Run Django via WSGI.
  application = django.core.handlers.wsgi.WSGIHandler()
  util.run_wsgi_app(application)

if __name__ == '__main__':
  main()