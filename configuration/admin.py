from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError

from .models import Config


class ConfigAdminForm(forms.ModelForm):
    class Meta:
        model = Config
        fields = '__all__'

    def clean(self):
        if not self.instance.pk and Config.objects.exists():
            raise ValidationError('There can be only one Config instance')
        return super().clean()


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    form = ConfigAdminForm
    list_display = ('name', 'home_title', 'about_title', 'services_title', 'start_time', 'email')

    def has_add_permission(self, request):
        # Disable add permission if a Config instance already exists
        if Config.objects.exists():
            return False
        return super().has_add_permission(request)
