from django.contrib import admin
from .models import Project
from django.utils.html import format_html


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'photo_tag')

    def photo_tag(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        return '-'
    photo_tag.short_description = 'Photo'


admin.site.register(Project, ProjectAdmin)
