from rest_framework import serializers
from .models import Category, Product, Variants, Color, Size, Images


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['name',
                  'code']


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = ['name',
                  'code']


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ["id",
                  "name",
                  "image",]


class VariantSerializer(serializers.ModelSerializer):

    color_data = ColorSerializer(source='color_id', read_only=True)
    size_data = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Variants
        fields = ['id',
                  'name',
                  'quantity',
                  'price',
                  'color_data',
                  'size_data',
                  'image_id',
                  'image'
                  ]

    def get_size_data(self, obj):
        return obj.get_size_data()

    def get_image(self, obj):
        request = self.context.get('request')
        if request:
            return obj.get_image_url(request)
        return None


class ProductSerializer(serializers.ModelSerializer):

    variants = serializers.SerializerMethodField('get_variants')
    images = serializers.SerializerMethodField('get_images')

    def get_variants(self, obj):
        serializer_context = {'request': self.context.get('request')}
        variants = obj.product_variants.all()
        return VariantSerializer(variants, many=True, context=serializer_context).data

    def get_images(self, obj):
        serializer_context = {'request': self.context.get('request')}
        images = obj.product_images.all()
        return ImagesSerializer(images, many=True, context=serializer_context).data

    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'name',
            'keywords',
            'description',
            'image',
            'images',
            'price',
            'compare_price',
            'stock',
            'minstock',
            'variant',
            'detail',
            'slug',
            'status',
            'created',
            'updated',
            'variants'
        ]
