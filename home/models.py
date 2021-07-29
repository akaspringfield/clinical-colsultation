from django.db import models
from django.utils import timezone

class Profile_Pic(models.Model):
    img = models.ImageField(upload_to='home/images')

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='home/images',)
    url = models.URLField(blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
