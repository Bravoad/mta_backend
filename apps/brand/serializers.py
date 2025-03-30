from rest_framework import serializers
from .models import Brand


class NestedBrandSerializer(serializers.ModelSerializer):
    """
    Этот сериализатор используется для вложенного отображения рекомендуемых брендов.
    Здесь выводятся базовые поля бренда.
    """
    class Meta:
        model = Brand
        fields = ['id', 'name_en', 'name_ru',
                  'short_description_en', 'short_description_ru', 'logo', 'picture', 'order']


class BrandSerializer(serializers.ModelSerializer):
    recommended_brands = NestedBrandSerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = ['id', 'name_en', 'slug', 'name_ru', 'logo', 'brand_image'
                  'short_description_en', 'short_description_ru', 'dynamic_description', 'picture', 'order',
                  'recommended_brands',
                  ]
