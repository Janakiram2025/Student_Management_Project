from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Teacher, Student

# Admin config for Teacher
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'email', 'phone',
        'teacher_id', 'designation', 'school_name'
    )
    search_fields = ('first_name', 'last_name', 'email', 'teacher_id', 'subjects')
    list_filter = ('designation', 'school_name')
    ordering = ('first_name', 'teacher_id')
    list_per_page = 25

# Admin config for Student
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'email', 'phone',
        'roll_number', 'department', 'year'
    )
    search_fields = ('first_name', 'last_name', 'email', 'roll_number')
    list_filter = ('department', 'year')
    ordering = ('first_name', 'roll_number')
    list_per_page = 25

# Register models
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
