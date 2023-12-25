from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    image = models.ImageField(upload_to="media/cars/categories", null=True, blank=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


class Brand(models.Model):
    name = models.CharField(max_length=20)
    country_of_origin = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}, {self.country_of_origin}"

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class Car(models.Model):
    class ENGINE_TYPE(models.TextChoices):
        DIESEL = "Diesel"
        GASOLINE = "Gasoline"
        ELECTRO = "Electro"
        GAS = "Gas"

    brand = models.ForeignKey(
        "cars.Brand", related_name="brand", on_delete=models.CASCADE
    )
    max_speed = models.PositiveSmallIntegerField(default=100, blank=False)
    acceleration_value = models.PositiveSmallIntegerField(default=5, blank=False)
    horse_power = models.PositiveSmallIntegerField(default=100, blank=False)
    engine_type = models.TextField(
        choices=ENGINE_TYPE.choices, default=ENGINE_TYPE.GASOLINE
    )
    category = models.ForeignKey(
        to="cars.Category", related_name="category", on_delete=models.CASCADE
    )
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to="media/cars/cars_images")

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return (
            f"{self.brand.name}, {self.max_speed} km/h, {self.acceleration_value} seconds, {self.engine_type}, "
            f"{self.category}, {self.description}"
        )


class FavoriteCars(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    car = models.ForeignKey(to="cars.Car", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Favorite Car"
        verbose_name_plural = "Favorite Cars"

    def __str__(self):
        return f"{self.user}"
