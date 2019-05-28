from django.shortcuts import render
from django.http import HttpResponse
from .models import Logo
from .serializers import LogoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class Logos(APIView):
    def get(self, request):
        logos = Logo.objects.all()
        serializer = LogoSerializer(logos, many=True)
        return Response(serializer.data)

