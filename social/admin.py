from django.contrib import admin
from .models import SocialLink


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('photo', 'link')
