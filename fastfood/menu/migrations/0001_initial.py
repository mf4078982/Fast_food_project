# Generated by Django 5.0.4 on 2024-11-15 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('food_item', models.CharField(max_length=255)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
