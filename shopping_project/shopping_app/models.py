from django.db import models


class Fruits(models.Model):
    fruit_name = models.CharField(max_length=15)
    fruit_price = models.CharField(max_length=15)
    img_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.fruit_name
