from django.contrib import admin
from .models import SourceOfGratitude


@admin.register(SourceOfGratitude)
class SourceOfGratitudeAdmin(admin.ModelAdmin):
    list_display = ("id", "text")
    search_fields = ("text",)
