from django.db import models
from phone_field import PhoneField


# Inspiration from https://stackoverflow.com/questions/7700487/how-to-model-a-postal-address
class USAddress(models.Model):
    street = models.TextField()
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=11)


class Consumer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneField()  # Using 3rd-party Model until it adds comlexity
    date_joined = models.DateField(auto_now_add=True)


class Property(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    address = USAddress()
    annual_kwh = models.PositiveIntegerField()
    date_posted = models.DateField(auto_now_add=True)


class Installer(models.Model):
    name = models.CharField(max_length=100)
    address = USAddress()
    age = models.PositiveSmallIntegerField()
    date_joined = models.DateField(auto_now_add=True)


class Quote(models.Model):
    # Retain for analysis (subject to installer and Consumer privacy policy)
    installer = models.ForeignKey(Installer, null=True, on_delete=models.SET_NULL)
    consumer = models.ForeignKey(Consumer, null=True, on_delete=models.SET_NULL)
    cost = models.DecimalField(max_digits=11, decimal_places=2)
    panel_brand = models.CharField(max_length=100)
    panel_type = models.CharField(max_length=255)
    date_offered = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
