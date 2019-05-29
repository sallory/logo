from django.shortcuts import render
from django.http import HttpResponse
from .models import Logo, LogoTag
from .serializers import LogoSerializer, LogoTagSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class Logos(APIView):
    def get(self, request):
        q = self.request.query_params.get('q', None)
        logos = Logo.objects.filter(logotags__tag__name=q)
        serializer = LogoSerializer(logos, many=True)
        return Response(serializer.data)