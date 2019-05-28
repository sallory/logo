from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=32)
    creation_date = models.DateTimeField()
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name


class Logo(models.Model):
    name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=None)
    creation_date = models.DateTimeField()
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=16)
    logo = models.ForeignKey(Logo, on_delete=None)
    creation_date = models.DateTimeField()
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name


class LogoTag(models.Model):
    logo = models.ForeignKey(Logo, on_delete=None)
    tag = models.ForeignKey(Tag, on_delete=None)
    creation_date = models.DateTimeField()

    def __str__(self):
        return self.logo

class LogoFormat(models.Model):
    logo = models.ForeignKey(Logo, on_delete=None)
    extension = models.CharField(max_length=16)
    image_url = models.CharField(max_length=64)

    def __str__(self):
        return self.logo
    