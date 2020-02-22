from django.contrib.auth.models import *
from django.db import models


# Create your models here.

# class User(AbstractUser):
#     date_of_birth = models.DateField(blank=True, null=True)
#     time_created = models.DateTimeField(auto_created=True, default=timezone.now)
#
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'
#
#         ordering = ['-time_created']
#
#     def __str__(self):
#         return '{} {}'.format(self.first_name, self.last_name)
