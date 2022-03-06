from django.contrib import admin

from jibou.models import Task
from .models import *
# Register your models here.
admin.site.register(Task)