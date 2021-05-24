from __future__ import absolute_import

from django.contrib import admin

from .models import Content


class ContentAdmin(admin.ModelAdmin):
    model = Content
    list_display = ('name', 'season', 'series')


admin.site.register(Content, ContentAdmin)
