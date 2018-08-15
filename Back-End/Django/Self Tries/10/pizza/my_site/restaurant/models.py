from django.db import models

# Create your models here.
import datetime

class Item(models.Model):
    # price = models.IntegerField()
    # Price 		- int choice field
    LARGE = 'L'
    MEDIUM = 'M'
    SMALL = 'S'

    SIZE_CHOICES = (
                    (LARGE, 'Large'),
                    (MEDIUM, 'Medium'),
                    (SMALL, 'Small')
                    )
                
    size = models.CharField(max_length=1, 
                            choices=SIZE_CHOICES,
                            default=SMALL)

    discount = models.FloatField()
    promotion = models.FloatField()
    promotion_available = models.BooleanField(default=False)

    preperation_time = models.DurationField(default=datetime.timedelta(minutes=30))

    servings = models.IntegerField(default=1)
    description = models.TextField()
    qoute = models.TextField()
    calories = models.FloatField()
    quantity = models.IntegerField()
    item_name = models.CharField(max_length=200)


class Pizza(Item):
    inch = models.FloatField()

    CHEEZE = 'C'
    SAUSAGE = 'S'
    PRAWN = 'P'

    TOPPING_CHOICES = (
                        (CHEEZE, 'Cheeze'),
                        (SAUSAGE, 'Sausages'),
                        (PRAWN, 'Prawns')
                        ) 
    topping = models.CharField(max_length=1, 
                            choices=TOPPING_CHOICES,
                            default=None)
    crust = models.TextField()
    ingredients = models.TextField()


class Drink(Item):
    DEW = 'D'
    COKE = 'C'
    WATER = 'W'

    DRINKS_CHOICES = (
                        (DEW, 'Mountain New'),
                        (COKE, 'Coca Cola'),
                        (WATER, 'Mineral Water')
                        ) 
    drinks_ordered = models.CharField(max_length=1, 
                            choices=DRINKS_CHOICES,
                            default=None)

