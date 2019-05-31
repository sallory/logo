from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=32)
    creation_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=16)
    creation_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name


class Logo(models.Model):
    name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=None)
    creation_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=256, null=True, blank=True)
    tags = models.ManyToManyField(
        Tag,
        through='LogoTag',
        through_fields=('logo', 'tag')
    )

    def __str__(self):
        return self.name


class LogoTag(models.Model):
    logo = models.ForeignKey(Logo, on_delete=None, related_name='logotags')
    tag = models.ForeignKey(Tag, on_delete=None)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.logo.name


class LogoFormat(models.Model):
    logo = models.ForeignKey(Logo, on_delete=None, related_name='formats')
    extension = models.CharField(max_length=16)
    image_url = models.CharField(max_length=64)

    def __str__(self):
        return self.logo.name
    