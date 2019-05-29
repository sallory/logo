from django.shortcuts import render
from django.http import HttpResponse
from .models import Logo, LogoTag
from .serializers import LogoSerializer, LogoTagSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class Logos(APIView):
    def get(self, request):
        tag = self.request.GET.getlist('tag', None)
        logos = {}
        if tag:
            logos = Logo.objects.filter(logotags__tag__name__in=tag)
        serializer = LogoSerializer(logos, many=True)
        return Response(serializer.data)