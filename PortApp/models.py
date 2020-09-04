from django.db import models
from datetime import datetime

# Create your models here.
class article(models.Model):
    Title = models.CharField(max_length=100)
    Job = models.CharField(max_length=100,default='')
    Description = models.TextField()
    Image = models.ImageField(upload_to='static/images',default='')