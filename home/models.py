from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=500)
    logo = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=500)
    logo = models.CharField(max_length=50)
    slug = models.CharField(max_length=500)
    link = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length=500)
    logo = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Chef(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    post = models.TextField(blank=True)
    comment = models.TextField()
    stars = models.ImageField(default=5)

    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    twitter = models.URLField(max_length=100, blank=True)
    facebook = models.URLField(max_length=100, blank=True)
    instagram = models.URLField(max_length=100, blank=True)
    youtube = models.URLField(max_length=100, blank=True)
    linkedin = models.URLField(max_length=100, blank=True)

    def __str__(self):
        return self.address