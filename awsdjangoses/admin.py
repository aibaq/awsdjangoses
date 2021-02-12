from django.contrib import admin

from . import models


@admin.register(models.AwsBlackList)
class AwsBlackListAdmin(admin.ModelAdmin):
    list_display = ('email', 'bounce', 'complaint')
    list_filter = ('bounce', 'complaint')
    search_fields = ('email',)
