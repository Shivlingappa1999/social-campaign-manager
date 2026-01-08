import os
import requests
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum

from .models import Campaign
from .serializers import CampaignSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


@api_view(["GET"])
def dashboard_api(request):
    total = Campaign.objects.count()
    active = Campaign.objects.filter(status="Active").count()
    budget = Campaign.objects.aggregate(total_budget=Sum("budget"))["total_budget"] or 0

    return Response({
        "total_campaigns": total,
        "active_campaigns": active,
        "total_budget": budget
    })


@api_view(["GET"])
def weather_api(request, city):
    api_key = "4d9f05ac5c692b62ccc7994b180267e9"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url)
    return Response(res.json())
