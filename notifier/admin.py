# coding=utf-8

from django.contrib import admin

from .models import DbTemplate


class DbTemplateAdmin(admin.ModelAdmin):
    pass


admin.site.register(DbTemplate, DbTemplateAdmin)
