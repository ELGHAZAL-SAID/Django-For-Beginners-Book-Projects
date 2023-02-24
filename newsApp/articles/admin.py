from http.client import ImproperConnectionState
from django.contrib import admin
from .models import Article
# Register your models here.

admin.site.register(Article)