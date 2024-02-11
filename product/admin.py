from django.contrib import admin
from django.forms import inlineformset_factory
from product.models import Product, Image, Category, Unit


class ImageInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = Image
    extra = 1  # Number of empty forms to display for adding new images


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


class UnitAdmin(admin.ModelAdmin):
    list_display = ('product', 'value', 'unit_name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Unit, UnitAdmin)
