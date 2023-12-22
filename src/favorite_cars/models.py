from django.contrib.auth import get_user_model
from django.db import models


class FavoriteCars(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    car = models.ManyToManyField(to="cars.Car")

    class Meta:
        verbose_name = "Favorite Car"
        verbose_name_plural = "Favorite Cars"

    def __str__(self):
        return f"{self.user}"
