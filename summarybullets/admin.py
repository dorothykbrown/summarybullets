from django.contrib import admin
from .models import Text, Summary, BulletPoint

admin.site.register([BulletPoint, Text, Summary])