from django.db import models

# Create your models here.
class profile(models.Model):
    f_name = models.CharField(max_length=25)
    l_name = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.TextField(max_length=15)

    def __str__(self):
        return self.name
