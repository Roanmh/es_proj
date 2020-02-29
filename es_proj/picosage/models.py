from django.db import models
from phone_field import PhoneField


# Inspiration from https://stackoverflow.com/questions/7700487/how-to-model-a-postal-address
class USAddress(models.Model):
    street = models.TextField()
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.street} {self.city}, {self.state} {self.zip_code}"


class Consumer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneField()  # Using 3rd-party Model until it adds comlexity
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Property(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    # Reset db to get rid of null setting: https://stackoverflow.com/questions/42150499/how-do-i-delete-db-sqlite3-in-django-1-9-to-start-from-scratch/42150639
    address = models.ForeignKey(USAddress, on_delete=models.PROTECT, null=True)  # TODO: null-False
    annual_kwh = models.PositiveIntegerField()
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.consumer.first_name} {self.consumer.last_name} at {self.address.street}"


class Installer(models.Model):
    name = models.CharField(max_length=100)
    # Reset db to get rid of null setting: https://stackoverflow.com/questions/42150499/how-do-i-delete-db-sqlite3-in-django-1-9-to-start-from-scratch/42150639
    address = models.ForeignKey(USAddress, on_delete=models.PROTECT, null=True)  # TODO: null=False
    date_started = models.DateField(null=True)  # TODO: null=False
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    # Retain for analysis (subject to installer and Consumer privacy policy)
    installer = models.ForeignKey(Installer, null=True, on_delete=models.SET_NULL)
    property = models.ForeignKey(Property, null=True, on_delete=models.SET_NULL)
    cost = models.DecimalField(max_digits=11, decimal_places=2)
    panel_brand = models.CharField(max_length=100)
    panel_type = models.CharField(max_length=255)
    date_offered = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.installer.name} for {self.property.address.street}"
