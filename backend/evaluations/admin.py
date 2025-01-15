from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'position', 'headshot')  # Adjust as needed
    search_fields = ['name', 'position']
    list_filter = ['position', 'team']
