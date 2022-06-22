from django.contrib import admin
from app.models import student
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ('id', 'cNumber', 'cName', 'cMajor', 'cGrade', 'ctime','cMail', 'cStatus')
    list_filter=('cName', 'cNumber')
    search_fields=('cName','cNumber',)
    ordering=('id',)
admin.site.register(student, studentAdmin)
