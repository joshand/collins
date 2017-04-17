# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from api.models import DockerJob, Result, Environment
from django_celery_beat.admin import PeriodicTask, CrontabSchedule
@admin.register(Environment)
class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'json',)


@admin.register(DockerJob)
class DockerJobAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'enabled', 'environment', 'image',)
    search_fields = ('id', 'image',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(DockerJobAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['task'].initial = 'api.tasks.run_image'
        return form

@admin.register(Result)
class ResponseAdmin(admin.ModelAdmin):
    list_display= ('id', 'jobId', 'result',)

# not needed on admin site as DockerJob inherits from PeriodicTask
admin.site.unregister(PeriodicTask)
# crontabs are not currently supported
admin.site.unregister(CrontabSchedule)