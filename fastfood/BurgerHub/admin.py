from django.contrib import admin
from .models import MenuItem
# Register your models here.
@admin.register(MenuItem)
class MenuItemadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'category')