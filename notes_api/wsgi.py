import os
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notes_api.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "DevelopmentConfig")

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
