import random

from django.db import models


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=45, unique=True)
    description = models.TextField()
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    date_created = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if self.pk is None:
            # Check that account_number is_unique..
            is_unique = False
            while not is_unique:
                code = random.randrange(10000000, 99999999)  # 8 digits
                is_unique = (Item.objects.filter(code=code).count() == 0)
                self.code = code

        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
