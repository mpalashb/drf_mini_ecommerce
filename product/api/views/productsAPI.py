from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import (
    viewsets,
    filters,
)
from django_filters import rest_framework as drffilters

from rest_framework.response import Response
from rest_framework import generics, permissions, response, status
from product.models import (
    Product as ProductModel,
    Image as ProductImages,
    Category as ProductCategory,

)
from product.api.filters.filters import (
    ProductPriceFilter
)

from product.api.serailizers.products import (
    ProductSerializer,
    ProductCDUSerializer,
    ProductImageSerializers,
    ProductSerializerShort,
    ProductImageSerializerUD,
    CatSerializer,
)

# general public


class GetCategoryAPI(generics.ListAPIView):
    serializer_class = CatSerializer
    permission_classes = (
        permissions.AllowAny,
    )
    model = ProductCategory
    queryset = ProductCategory.objects.all()


class ProductsView(generics.ListAPIView):
    serializer_class = ProductSerializerShort
    model = ProductModel
    queryset = ProductModel.objects.all()
    permission_classes = (
        permissions.AllowAny,
    )


class ProductSearchView(ProductsView):
    filter_backends = (drffilters.DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ['name', 'description']
    filterset_class = ProductPriceFilter


class ProductCDUViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for creating, updating, and deleting products for admin only
    """

    serializer_class = ProductCDUSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    )

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            product = ProductModel.objects.get(pk=pk)
        except ProductModel.DoesNotExist:
            return Response({'detail': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        print(request.data)
        # print(request.data)
        serializer = self.serializer_class(
            instance=product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            product = ProductModel.objects.get(pk=pk)
        except ProductModel.DoesNotExist:
            return Response({'detail': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving products for public
    """

    def list(self, request):
        queryset = ProductModel.objects.all()
        serializer = ProductSerializerShort(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ProductModel.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class ProductImagesUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductImageSerializerUD
    permission_classes = (
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    )
    model = ProductImages

    def get_queryset(self):
        return self.model.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
