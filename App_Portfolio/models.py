from django.db import models

# Create your models here.
class MO_projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'App_Portfolio/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name
