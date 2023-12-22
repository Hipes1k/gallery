from django.contrib import admin

from cars.models import AdditionalCharacteristics, Brand, Car, Category

admin.site.register([Car, AdditionalCharacteristics, Brand, Category])
