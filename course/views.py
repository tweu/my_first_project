from course.forms import BranchForm, GroupForm, StudentForm
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import *



# Create your views here.

def my_main_page(request):
    return render(request, 'course/my_page.html')



def branches_list(request):
    branches = Branch.objects.all()
    my_context = {'branches': branches}
    return render(request, 'course/branches-list.html', context = my_context)

def branch_details(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    groups = Group.objects.filter(branch=branch)
    context = {'branch': branch, 'groups': groups}
    return render(request, 'course/branch_detail.html', context=context)


def branches_create(request):
    if request.method == "POST":
        form = BranchForm(request.POST)
        if form.is_valid():
            branch = form.save()
            return redirect('branch_details', branch_id=branch.id)
    else:
        form = BranchForm()

    return render(request, 'course/branches_create.html', {'form': form})


def branch_edit(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)    
        if form.is_valid():
            branch = form.save()
            return redirect('branch_details', branch_id=branch.id)
    else:
        form = BranchForm(instance=branch)
    return render(request, 'course/branch_edit.html', {'form': form})

































def group_list(request):
    groups = Group.objects.all()
    my_context = {'groups': groups}
    return render(request, 'course/group-list.html', context = my_context)

def group_details(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    student = Student.objects.filter(group=group)
    context = {'group': group, 'student': student}
    return render(request, 'course/group_details.html', context=context)


def groups_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            return redirect('group_details', group_id = group.id)
    else:
        form = GroupForm()
    return render(request, 'course/groups_create.html', {'form': form})

def group_edit(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save()
            return redirect('group_details', group_id=group_id)
    else:
        form = GroupForm(instance=group)
    return render(request, 'course/group_edit.html', {'form': form})
































def student_list(request):
    student = Student.objects.all()
    my_context = {'students': student}
    return render(request, 'course/students-list.html', context = my_context)

def student_details(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    groups = Group.objects.filter(student=student)
    context = {'student': student, 'groups': groups}
    return render(request, 'course/student_detail.html', context = context) 

def students_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_details', student_id = student.id)
    else:
        form = StudentForm()
    return render(request, 'course/students_create.html', {'form': form})

def student_edit (request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('student_details', student_id=student.id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'course/student_edit.html', {'form': form})

