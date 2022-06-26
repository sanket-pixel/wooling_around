from django.db import models

# Create your models here.
class WoolItem(models.Model):
    brand = models.CharField(max_length=200,default="")
    product = models.CharField(max_length=200,default="")
    created = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0)
    currency = models.CharField(max_length=10, default='$')
    needle_size =  models.CharField(max_length=100, default='$')
    composition = models.CharField(max_length=200,default="")
    link = models.CharField(max_length=1000,default="")
