from rest_framework import viewsets
from .models import Partner
from .serializers import PartnerSerializer

class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only API для модели Partner.
    Позволяет выполнять GET-запросы для получения списка партнеров и детальной информации по партнеру.
    """
    queryset = Partner.objects.filter(is_displayed=True).order_by('order')
    serializer_class = PartnerSerializer
