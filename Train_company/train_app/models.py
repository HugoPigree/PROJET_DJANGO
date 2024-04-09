from django.db import models

class Train(models.Model):
    id = models.AutoField(primary_key=True)
    datetime = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    plan = models.ImageField(upload_to='img/')
