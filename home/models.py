from django.db import models

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateField()


class bicycle(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='photos')
    details = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default = False)