from django.contrib import admin

# Import our class #
from .models import Meeting

# Register your models here.
admin.site.register(Meeting)