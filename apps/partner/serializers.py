from rest_framework import serializers
from .models import Partner

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'name_en', 'name_ru', 'logo', 'order', 'is_displayed']
