from django.contrib import admin
from django.db import models
from django import forms
# Register your models here.
from .models import Application

admin.site.register(Application)
