from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, dashboard_api, weather_api

router = DefaultRouter()
router.register("campaigns", CampaignViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("dashboard/", dashboard_api),
    path("weather/<str:city>/", weather_api),
]
