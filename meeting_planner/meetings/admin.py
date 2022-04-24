from django.contrib import admin

# Import our class #
from .models import Meeting, Room

# Register your models here.
admin.site.register(Meeting)
admin.site.register(Room)