from django.contrib import admin
from django.contrib.admin.models import LogEntry


class AdminLog(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'action_time']


admin.site.register(LogEntry, AdminLog)
