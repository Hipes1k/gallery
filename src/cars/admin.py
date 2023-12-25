from django.contrib import admin

from cars.models import Brand, Car, Category, FavoriteCars

admin.site.register([Car, Brand, Category, FavoriteCars])
