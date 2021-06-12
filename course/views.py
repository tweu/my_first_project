from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def my_main_page(request):
    my_context ={'name': 'Max', 
        'my_list': [1,2,3,4,5]
       }
    return render(request, 'course/my_page.html', context=my_context)



def branches_list(request):
    branches = Branch.objects.all()
    my_context = {'branches': branches}
    return render(request, 'course/branches-list.html', context = my_context)

def branch_details(request, branch_id):
    branch = Branch.objects.get(id = branch_id)
    groups = Group.objects.filter(branch=branch)
    context = {'branch': branch, 'groups': groups}
    return render(request, 'course/branch_detail.html', context=context)

def group_list(request):
    groups = Group.objects.all()
    my_context = {'groups': groups}
    return render(request, 'course/group-list.html', context = my_context)

def group_details(request, group_id):
    group = Group.objects.get(id = group_id)
    student = Student.objects.filter(group=group)
    context = {'group': group, 'student': student}
    return render(request, 'course/group_details.html', context=context)

def student_list(request):
    student = Student.objects.all()
    my_context = {'students': student}
    return render(request, 'course/students-list.html', context = my_context)

def student_details(request, student_id):
    student = Student.objects.get(id = student_id)
    groups = Group.objects.filter(student=student)
    context = {'student': student, 'groups': groups}
    return render(request, 'course/student_detail.html', context = context) 

