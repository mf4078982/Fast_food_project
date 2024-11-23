from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    location = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    food_item = models.CharField(max_length=255)  # This will store the name of the ordered food
    order_date = models.DateTimeField(auto_now_add=True)
