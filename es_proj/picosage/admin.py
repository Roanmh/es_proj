from django.contrib import admin

from .models import USAddress, Consumer, Property, Installer, Quote

# Register your models here.
admin.site.register(USAddress)
admin.site.register(Consumer)
admin.site.register(Property)
admin.site.register(Installer)
admin.site.register(Quote)
