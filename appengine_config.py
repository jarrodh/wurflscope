import os
import logging

# Declare the Django version we need.
from google.appengine.dist import use_library
use_library("django", "1.2")

# Fail early if we can"t import Django 1.x.  Log identifying information.
import django
logging.info("django.__file__ = %r, django.VERSION = %r",
             django.__file__, django.VERSION)
assert django.VERSION[0] >= 1, "This Django version is too old"

# Custom Django configuration.
# NOTE: For obscure reasons, this must be repeated here as well as in
# appengine_config.py.  Without the duplication, we get tracebacks
# from Django complaining about ROOT_URLCONF when the first hit to a
# fresh process is /_ah/stats, and the second is /.
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
from django.conf import settings
settings._target = None
