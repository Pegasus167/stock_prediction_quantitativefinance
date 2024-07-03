from django.urls import path, include
from .views import CompanyViewSet,UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('Company', CompanyViewSet, basename='company')
router.register('users', UserViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
