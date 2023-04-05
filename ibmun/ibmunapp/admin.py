from django.contrib import admin
from .models import Announcements, Comment

# Register your models here.
admin.site.register(Announcements)
admin.site.register(Comment)