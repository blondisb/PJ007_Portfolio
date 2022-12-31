from django.db import models
import datetime

# Create your models here.
class MO_blogs(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='App_Blog/images')
    date = models.DateField(default = datetime.date.today)

    def __str__(self):
        return self.name
