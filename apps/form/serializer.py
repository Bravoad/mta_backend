from rest_framework import serializers
from .models import ContactForm
from django.conf import settings
import requests


def verify_recaptcha(recaptcha_response):
    url = "https://www.google.com/recaptcha/api/siteverify"
    payload = {
        'secret': settings.RECAPTCHA_SECRET_KEY,  # Укажите ваш секретный ключ в settings.py
        'response': recaptcha_response
    }
    response = requests.post(url, data=payload)
    result = response.json()
    return result.get('success', False)


class ContactFormSerializer(serializers.ModelSerializer):
    recaptcha = serializers.CharField(write_only=True)

    class Meta:
        model = ContactForm
        fields = ('name', 'phone', 'consent', 'recaptcha')

    def validate_recaptcha(self, value):
        if not verify_recaptcha(value):
            raise serializers.ValidationError("Invalid reCAPTCHA.")
        return value

    def create(self, validated_data):
        # Удаляем поле recaptcha, чтобы не сохранять его в модель
        validated_data.pop('recaptcha', None)
        return super().create(validated_data)
