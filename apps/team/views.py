from rest_framework import viewsets
from .models import Team
from .serializers import TeamSerializer


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    # Выводим только записи, помеченные для отображения
    queryset = Team.objects.filter(is_displayed=True).order_by('order')
    serializer_class = TeamSerializer
