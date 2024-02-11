from django_filters import rest_framework as filters
from product.models import Product


class ProductPriceFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_current_price = filters.NumberFilter(
        field_name="current_price", lookup_expr='gte')
    max_current_price = filters.NumberFilter(
        field_name="current_price", lookup_expr='lte')
    # min_discount_price = filters.NumberFilter(
    #     field_name="discount", lookup_expr='gte')
    # max_discount_price = filters.NumberFilter(
    #     field_name="discount", lookup_expr='lte')

    class Meta:
        model = Product
        fields = [
            'cat',
            'product_type',
            'status',
        ]
