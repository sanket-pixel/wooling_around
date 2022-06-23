from django.db import models

# Create your models here.

class WoolItem(models.Model):
    name =  models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    deliver_time = models.DateTimeField()
    needle_size = models.FloatField()
    composition = models.CharField(max_length=200)

