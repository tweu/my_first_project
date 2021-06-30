from course.models import Branch
from django.contrib import admin
from .models import Branch
from .models import Group
from .models import Student
from .models import Course
# Register your models here.

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')
    list_filter = ('creator', 'manager')
    raw_id_fields = ('creator', )

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch')
    search_fields = ('name', 'branch', 'course')
    list_filter = ('creator', 'course' )
    raw_id_fields = ('creator', )

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'gender', 'group', 'creator')
    search_fields = ('name', 'address', 'phone_number', 'gender')
    list_filter = ('name', 'address', 'phone_number', 'gender', 'courses', 'group', 'creator')
    raw_id_fields = ('creator', )       

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    list_filter = ('creator', )
    raw_id_fields = ('creator', )

admin.site.register(Branch, BranchAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)