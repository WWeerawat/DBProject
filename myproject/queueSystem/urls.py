from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("createQueue/<str:pk>", views.createQueue, name="createQueue"),
]
