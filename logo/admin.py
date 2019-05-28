from django.contrib import admin

# Register your models here.

from .models import Logo, Tag, LogoFormat, LogoTag, Category

admin.site.register(Logo)
admin.site.register(Tag)
admin.site.register(LogoFormat)
admin.site.register(LogoTag)
admin.site.register(Category)