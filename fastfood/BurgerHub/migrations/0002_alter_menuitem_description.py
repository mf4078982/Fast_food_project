# Generated by Django 5.0.4 on 2024-11-28 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BurgerHub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]
