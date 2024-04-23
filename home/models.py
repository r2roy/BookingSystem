from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=500)
    logo = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=500)
    logo = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    price = models.CharField(max_length=500, default=5)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Chef(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    twitter = models.URLField(max_length=100, blank=True)
    facebook = models.URLField(max_length=100, blank=True)
    instagram = models.URLField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    feedback = models.TextField(blank=True)
    role = models.CharField(max_length=500)

    def __str__(self):
        return self.name




