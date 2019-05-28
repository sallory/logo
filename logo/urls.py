from django.urls import path

from . import views

urlpatterns = [
    path('api/v1/logos', views.Logos.as_view(), name="logos"),
]
