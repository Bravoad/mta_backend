from rest_framework import serializers
from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name_en', 'name_ru', 'staff_en', 'staff_ru', 'picture', 'order', 'is_displayed']
