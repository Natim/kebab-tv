from os.path import splitext

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify
from admin_ordering.models import OrderableModel


def category_upload_to(instance, filename):
    _, ext = splitext(filename)
    if not ext:
        ext = ".jpg"
    return f"uploads/category_{slugify(instance.name)}{ext}"


class Category(OrderableModel):
    name = models.CharField(max_length=75)
    illustration = models.ImageField(upload_to=category_upload_to, blank=True, null=True)

    class Meta:
        ordering = ["ordering"]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Product(OrderableModel):
    name = models.CharField(max_length=75)
    priceEuroCents = models.IntegerField(
        validators=[MaxValueValidator(9999), MinValueValidator(1)],
        verbose_name="Price in euro cents",
    )
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["ordering"]


class Screen(OrderableModel):
    name = models.CharField(max_length=75)
    title = models.CharField(max_length=150)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["ordering"]
