from rest_framework import serializers

from .models import Logo, LogoFormat, LogoTag

class LogoFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogoFormat
        fields = ('logo', 'extension', 'image_url')


class LogoTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogoTag
        fields = ('logo', 'tag')


class LogoSerializer(serializers.ModelSerializer):
    formats = LogoFormatSerializer(many=True, read_only=True)
    logotags = LogoTagSerializer(many=True, read_only=True)

    class Meta:
        model = Logo
        fields = ('name', 'category', 'formats', 'logotags')
        read_only_fields = ('name','category', 'formats', 'logotags')