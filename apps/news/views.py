from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer

class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet, который возвращает только те новости,
    у которых is_displayed=True.
    """
    queryset = News.objects.filter(is_displayed=True).order_by('-published_at')
    serializer_class = NewsSerializer
