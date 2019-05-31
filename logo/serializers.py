from rest_framework import serializers
from .models import Logo, LogoFormat, Tag, LogoTag

class LogoFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogoFormat
        fields = ('extension', 'image_url')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class LogoSerializer(serializers.ModelSerializer):
    formats = LogoFormatSerializer(many=True)
    tags = TagSerializer(many=True)
    category = serializers.CharField(max_length=32)

    class Meta:
        model = Logo
        fields = ('name', 'category', 'formats', 'tags')

    def create(self, validated_data):
        category = validated_data['category']
        name = validated_data['name']
        tags = validated_data['tags']
        formats = validated_data['formats']
        logo, created = Logo.objects.get_or_create(name=name, category=category)
        for format_data in formats:
            new_tag, created = LogoFormat.objects.get_or_create(logo=logo ,**format_data)
        for tag_data in tags:
            tag, created = Tag.objects.get_or_create(name=tag_data['name'])
            logo_tag, created = LogoTag.objects.get_or_create(logo=logo, tag=tag)
        return logo
