from django.urls import path
from rest_framework.routers import DefaultRouter
from product.api.views.productsAPI import (
    ProductsView,
    ProductSearchView,
    ProductViewSet,
    ProductCDUViewSet,
    ProductImagesUD,
    GetCategoryAPI,
)


app_name = 'prduct'

urlpatterns = [
    path('products-paginate/', ProductsView.as_view(), name='all-products'),
    path('products-query/', ProductSearchView.as_view(), name='search-products'),
]

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'product-admin', ProductCDUViewSet, basename='product-admin')
urlpatterns += router.urls

urlpatterns += [
    path('images/<int:pk>/', ProductImagesUD.as_view(),
         name='product-image-ud')  # product update, retrive and delete (POST, GET, Delete)
]
# generate category
urlpatterns += [
    path('all-category/', GetCategoryAPI.as_view(),
         name='gen-cat')  # getting category as public api
]
