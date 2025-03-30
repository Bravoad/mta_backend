from rest_framework.views import APIView
from rest_framework.response import Response
from constance import config


class ConstanceConfigAPIView(APIView):
    """
    APIView для получения текущих настроек из constance.
    """
    def get(self, request, format=None):
        data = {
            'SITE_NAME_EN': config.SITE_NAME_EN,
            'DESCRIPTION_EN': config.DESCRIPTION_EN,
            'DESCRIPTION_SMAIL_EN': config.DESCRIPTION_SMAIL_EN,
            'SITE_NAME_RU': config.SITE_NAME_RU,
            'DESCRIPTION_RU': config.DESCRIPTION_RU,
            'DESCRIPTION_SMAIL_RU': config.DESCRIPTION_SMAIL_RU,
        }
        return Response(data)
