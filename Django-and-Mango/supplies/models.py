from django.db import models
from django.conf import settings
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=350)
    quantity = models.IntegerField()
    rate = models.IntegerField()
    requirements  = models.IntegerField()
    order = models.BooleanField(default = False)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Vendor(models.Model):
    item = models.ForeignKey('Item',on_delete=models.CASCADE)
    name = models.CharField(max_length=350)
    contact = models.CharField(max_length=10)
    area = models.TextField()
    available = models.BooleanField(default = False)
    slug = models.SlugField()

    def __str__(self):
        return self.name
