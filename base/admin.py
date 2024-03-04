from django.contrib import admin
from base.models import Task

# class TaskAdmin(admin.ModelAdmin):
#     fieldsets=[]
# Register your models here.
admin.site.register(Task)