# Generated by Django 3.0.8 on 2020-07-16 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0002_fruits_fruit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruits',
            name='fruit_image',
            field=models.ImageField(max_length=2083, upload_to=''),
        ),
    ]