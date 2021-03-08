from newsletter.models import Newsletter, Subcriber
from django.contrib import admin
from django.contrib.admin.decorators import register

admin.site,register(Newsletter)
admin.site,register(Subcriber)
