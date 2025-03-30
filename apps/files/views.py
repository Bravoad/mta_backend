from rest_framework.generics import ListAPIView
from .models import Files
from .serializers import FilesSerializer


class FilesListAPIView(ListAPIView):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer
