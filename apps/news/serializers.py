from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'id',
            'image',
            'short_text_en',
            'short_text_ru',
            'is_displayed',
            'published_at',
        ]
