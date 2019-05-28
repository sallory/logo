from rest_framework import serializers
from django.db.models import F

from .models import Logo

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ('name','category',)
        read_only_fields = ('name','category',)