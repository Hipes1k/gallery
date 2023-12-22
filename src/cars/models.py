from django.db import models


class Category(models.Model):
    image = models.ImageField(upload_to="media/cars/categories", null=True, blank=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return f"{self.name}"


class Brand(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=10)
    year_of_issue = models.PositiveSmallIntegerField(default=2000, blank=False)

    def __str__(self):
        return f"{self.brand} {self.model}, {self.year_of_issue} year"

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class AdditionalCharacteristics(models.Model):
    class ENGINE_TYPE(models.TextChoices):
        DIESEL = "Diesel"
        GASOLINE = "Gasoline"
        ELECTRO = "Electro"
        GAS = "Gas"

    brand = models.OneToOneField(Brand, on_delete=models.CASCADE)
    max_speed = models.PositiveSmallIntegerField(default=100, blank=False)
    one_to_hundred = models.PositiveSmallIntegerField(default=5, blank=False)
    usage = models.PositiveSmallIntegerField(default=15, blank=False)
    engine_capacity = models.FloatField(default=1.6, blank=False)
    engine_type = models.TextField(
        choices=ENGINE_TYPE.choices, default=ENGINE_TYPE.GASOLINE
    )

    def __str__(self):
        return (
            f"{self.brand}, {self.max_speed} KM/H, {self.one_to_hundred} sec, "
            f"{self.usage} L/100km, "
            f"{self.engine_capacity} L^3, {self.engine_type}"
        )

    class Meta:
        verbose_name = "Additional Chars"
        verbose_name_plural = "Additional Chars"


class Car(models.Model):
    characteristics = models.OneToOneField(
        AdditionalCharacteristics, on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        to="cars.Category", related_name="category", on_delete=models.CASCADE
    )
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="media/cars/cars_images")

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Car"

    def __str__(self):
        return f"{self.category}, {self.characteristics}"
