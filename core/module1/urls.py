from django.urls import path
from .views_ui import *

urlpatterns = [
    path("", campaign_list),
    path("create/", campaign_create),
    path("edit/<int:id>/", campaign_edit),
    path("delete/<int:id>/", campaign_delete),
]
