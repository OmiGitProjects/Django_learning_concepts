from django.contrib import admin
from .models import Student

# class StudentAdmin(admin.ModelAdmin):
#     # list_display = ('id', 'name', 'email', 'password')
#     list_display = ('name', 'email', 'password')
# admin.site.register(Student, StudentAdmin)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')