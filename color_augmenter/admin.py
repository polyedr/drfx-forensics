from django.contrib import admin
from .models import IllustrationSet, Image


class InlineImage(admin.TabularInline):
    model = Image


class IllustrationSetAdmin(admin.ModelAdmin):
    inlines = [InlineImage]


# from .models import *
admin.site.register(IllustrationSet, IllustrationSetAdmin)
