from django.core.exceptions import ValidationError
from django.db import models


class Config(models.Model):
    name = models.CharField(max_length=255)
    home_title = models.CharField(max_length=255)
    home_bg_photo = models.ImageField(upload_to='home_bg_photos/', null=True, blank=True)
    cv_file = models.FileField(upload_to='cv_files/')
    about_title = models.CharField(max_length=255)
    about_description = models.TextField()
    about_photo = models.ImageField(upload_to='about_photos/')
    services_title = models.CharField(max_length=255)
    services_subtitle = models.CharField(max_length=255)
    services_description = models.TextField()
    start_time = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk and Config.objects.exists():
            # Prevent more than one row from being saved
            raise ValidationError('There can be only one Config instance')
        return super(Config, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        if cls.objects.exists():
            return cls.objects.first()
        return cls()
