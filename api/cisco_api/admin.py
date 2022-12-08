from django.contrib import admin
from .models import category, blog

# Registraremos todos los modelos creados en models.py.
admin.site.register(category)
admin.site.register(blog)
