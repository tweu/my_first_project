from course.models import Branch
from django.contrib import admin
from .models import Branch
from .models import Group
from .models import Student

# Register your models here.


admin.site.register(Branch)
admin.site.register(Group)
admin.site.register(Student)