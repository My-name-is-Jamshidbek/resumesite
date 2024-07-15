from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    url = models.URLField(max_length=255, default='/')
    photo = models.ImageField(upload_to='project_photos/')

    def __str__(self):
        return self.name
