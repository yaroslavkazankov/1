from django.contrib import admin

from .models import Student, Teacher


# class TeacherInline(admin.TabularInline):
#     model = Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
    # inlines = [TeacherInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

