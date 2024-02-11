# yourapp/models.py
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Category(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return f"{self.name} | PK: {self.pk}"


class Unit(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product = GenericForeignKey('content_type', 'object_id')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    unit_name = models.CharField(max_length=10)  # e.g., gr, kg, liter, etc.

    def __str__(self):
        return f"{self.value} {self.unit_name} for {self.product}"


class Product(models.Model):
    CHOICES = (('trending', 'Trending'), ('normal', 'Normal'))

    name = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='product_images/thumbnail/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(
        blank=True, null=True)  # should be percentage

    cat = models.ManyToManyField(Category)
    status = models.BooleanField(default=True)
    left = models.IntegerField(blank=True, null=True)
    product_type = models.CharField(
        choices=CHOICES, default='normal', max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product.name} - {self.alt_text}"
