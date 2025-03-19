from django.contrib import admin

# Register your models here.
from . import models

admin.site_header = 'Blog Admin'
admin.site_title = 'Blog Admin Area'

admin.site.register(models.Post)
