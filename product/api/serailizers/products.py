from rest_framework import serializers
from product.models import Product, Category, Image
# -------------------------------------------------------
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# -------------------------------------------------------


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name'
        ]


class ProductSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "thumbnail",
            "price",
            "current_price",
            "discount",
            "cat",
            "status",
            "product_type",
        )


class ProductImageSerializerUD(serializers.ModelSerializer):
    product = ProductSerializerShort(read_only=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Image
        fields = '__all__'


class ProductImageSerializers(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    cat = CatSerializer(many=True)
    images = ProductImageSerializers(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductCDUSerializer(serializers.ModelSerializer):
    images = ProductImageSerializers(many=True, required=False)
    image_fields = serializers.ListField(
        child=serializers.ImageField(), required=False)
    image_ids = serializers.ListField(
        child=serializers.DictField(), required=False
    )

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        # validated_data.pop is required for remove this fields \
        #   that doesn't support by model but the inmemory files are present there
        image_fields = validated_data.pop('image_fields', [])
        product_instance = super().create(validated_data)

        # Handle the images
        for image in image_fields:
            Image.objects.create(product=product_instance, image=image)

        return product_instance

    # creating alt text for images and update product information expect images file
    def update(self, instance, validated_data):
        image_ids = validated_data.pop('image_ids', [])

        instance = super().update(instance, validated_data)

        for image_id_data in image_ids:
            image_id = image_id_data.get('id')
            image_alt_text = image_id_data.get('alt_text')
            # product_id = image_id_data.get('product')

            # Check if the image_id exists, and update or create accordingly
            if image_id:
                image_instance = Image.objects.get(id=image_id)
                image_instance.alt_text = image_alt_text
                image_instance.save()
            else:
                Image.objects.create(product=instance, alt_text=image_alt_text)

        return instance
