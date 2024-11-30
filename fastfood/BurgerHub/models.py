from django.db import models

# Create your models here.
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[
        ('burger', 'Burger'),
        ('pizza', 'Pizza'),
        ('drink', 'Drink'),
    ])
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return self.name
