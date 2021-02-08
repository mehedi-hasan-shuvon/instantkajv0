from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=20, default="FirstName")
    last_name = models.CharField(max_length=20, default="LastName")
    email = models.EmailField()
    password = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.first_name} {self.last_name} -- {self.email}'