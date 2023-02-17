from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
    

class Order(models.Model):
    items = models.ManyToManyField(Item)
