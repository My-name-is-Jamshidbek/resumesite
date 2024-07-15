from django.db import models


class SocialLink(models.Model):
    photo = models.CharField(max_length=255)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.link
