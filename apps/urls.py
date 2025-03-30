from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .brand.views import BrandViewSet
from .config.views import ConstanceConfigAPIView
from .files.views import FilesListAPIView
from .news.views import NewsViewSet
from .team.views import TeamViewSet
from .partner.views import PartnerViewSet
from .form.views import ContactFormViewSet
router = DefaultRouter()
router.register(r'brands', BrandViewSet, basename='brands')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'team', TeamViewSet, basename='team')
router.register(r'partners', PartnerViewSet, basename='partners')
router.register(r'contact-form', ContactFormViewSet, basename='contact-form')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/constance/', ConstanceConfigAPIView.as_view(), name='constance-config'),
    path('files/', FilesListAPIView.as_view(), name='files-list'),
]
