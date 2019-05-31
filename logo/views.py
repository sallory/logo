from django.shortcuts import render
from django.http import HttpResponse
from .models import Logo, Category, Tag, LogoTag
from .serializers import LogoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination


class Logos(APIView):
    def get(self, request):
        tag = self.request.GET.getlist('tag', None)
        q = self.request.query_params.get('q', None)
        logos = Logo.objects.all()
        if tag:
            logos = logos.filter(logotags__tag__name__in=tag).distinct()
        if q:
            logos = logos.filter(name=q)
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(logos, request)
        serializer = LogoSerializer(result_page, many=True, context={'request':request})
        return Response(serializer.data)

    def post(self, request):
        serializer = LogoSerializer(data=request.data)
        if serializer.is_valid():
            category_name = serializer.validated_data['category']
            category, created = Category.objects.get_or_create(name=category_name)
            serializer.save(category=category)
            return Response(serializer.data)
        return Response(serializer.errors)
        