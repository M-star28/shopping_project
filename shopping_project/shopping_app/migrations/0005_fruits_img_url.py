# Generated by Django 3.0.8 on 2020-07-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0004_remove_fruits_fruit_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruits',
            name='img_url',
            field=models.CharField(default='', max_length=2083),
            preserve_default=False,
        ),
    ]
