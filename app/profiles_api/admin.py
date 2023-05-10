from django.contrib import admin
from profiles_api import models

# Registers UserProfile to admin site
admin.site.register(models.UserProfile)
