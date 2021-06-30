from rest_framework.response import Response
from course.serializers import BranchSerializer, GroupSerializer, StudentSerializer
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from rest_framework import serializers
from course.forms import BranchForm, GroupForm, StudentForm, CourseForm
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import random
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.























def my_main_page(request):
    return render(request, 'course/my_page.html')





























def branches_list(request):
    branches = Branch.objects.all()
    my_context = {'branches': branches}
    return render(request, 'course/branches-list.html', context = my_context)

class BranchListView(ListView):
    model = Branch
    template_name = 'course/branches-list.html'
    context_object_name = 'branches'

def branch_details(request, branch_id):
    branch = get_object_or_404(Branch, pk=branch_id)
    groups = Group.objects.filter(branch=branch)
    context = {'branch': branch, 'groups': groups}
    return render(request, 'course/branch_detail.html', context=context)


class BranchDetailView(DetailView):
    model = Branch
    template_name = 'course/branch_detail.html'
    context_object_name = 'branch'
    pk_url_kwarg = 'branch_id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.filter(branch = self.object)
        return context

@login_required
def branches_create(request):
    if request.method == "POST":
        form = BranchForm(request.POST, request.FILES)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.creator = request.user
            branch.save()
            return redirect('branch_details', branch_id=branch.id)
    else:
        form = BranchForm()

    return render(request, 'course/branches_create.html', {'form': form})

class BranchCreateView(LoginRequiredMixin,CreateView):
    model = Branch
    fields = ['name', 'address', 'photo']
    template_name='course/branches_create.html'
    login_url = '/user/login/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())




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


class BranchUpdateView(LoginRequiredMixin,UpdateView):
    model = Branch
    fields = ['name', 'address', 'photo']
    template_name = 'course/branch_edit.html'
    pk_url_kwarg = 'branch_id'
    login_url = '/user/login/'

def branch_delete(request, branch_id):
    query = Branch.objects.get(pk=branch_id)
    query.delete()
    return HttpResponseRedirect("/course/branches/")

class BranchDeleteView(LoginRequiredMixin,DeleteView):
    model = Branch
    pk_url_kwarg = 'branch_id'
    success_url = reverse_lazy('branches_list')
    login_url = '/user/login/'

def branch_photo(request, branch_id):
    getphoto = Branch.objects.get(id = branch_id)
    return HttpResponseRedirect("/course/photo")

def branch_random(request):
    branches = Branch.objects.all()
    random_branch = random.choice(branches)
    my_context = {'branch': random_branch}
    return render(request, 'course/branch_detail.html', context=my_context)



























def group_list(request):
    groups = Group.objects.all()
    my_context = {'groups': groups}
    return render(request, 'course/group-list.html', context = my_context)

class GroupListView(ListView):
    model = Group
    template_name = 'course/group-list.html'
    context_object_name = 'groups'


def group_details(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    student = Student.objects.filter(group=group)
    context = {'group': group, 'student': student}
    return render(request, 'course/group_details.html', context=context)

class GroupDetailView(DetailView):
    model = Group
    template_name = 'course/group_details.html'
    context_object_name = 'group'
    pk_url_kwarg = 'group_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.filter(group=self.object)
        return context
    


def groups_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            group = form.save()
            return redirect('group_details', group_id = group.id)
    else:
        form = GroupForm()
    return render(request, 'course/groups_create.html', {'form': form})

class GroupCreateNew(LoginRequiredMixin,CreateView):
    model = Group
    fields = ['name', 'branch', 'photo']
    template_name='course/groups_create.html'
    login_url = '/user/login/'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



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

class GroupUpdateNew(LoginRequiredMixin,UpdateView):
    model = Group
    fields = ['name', 'branch', 'photo']
    template_name = 'course/group_edit.html'
    pk_url_kwarg = 'group_id'
    login_url = '/user/login/'


def group_delete(request, group_id):
    query = Group.objects.get(pk=group_id)
    query.delete()
    return HttpResponseRedirect("/course/groups")


class GroupDeleteView(LoginRequiredMixin,DeleteView):
    model = Group
    pk_url_kwarg = 'group_id'
    success_url = reverse_lazy('groups_list')
    login_url = '/user/login/'

def group_random(request):
    groups = Group.objects.all()
    random_group = random.choice(groups)
    my_context = {'group': random_group}
    return render(request, 'course/group_details.html', context=my_context)



























def student_list(request):
    student = Student.objects.all()
    my_context = {'students': student}
    return render(request, 'course/students-list.html', context = my_context)

class StudentListView(ListView):
    model = Student
    template_name = 'course/students-list.html'
    context_object_name = 'students'


def student_details(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    courses = student.courses.all()
    groups = Group.objects.filter(student=student)
    context = {'student': student, 'groups': groups, 'courses': courses}
    return render(request, 'course/student_detail.html', context = context) 

class StudentDetailView(DetailView):
    model = Student
    template_name = 'course/student_detail.html'
    context_object_name = 'student'
    pk_url_kwarg = 'student_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.object
        courses = student.courses.all()
        context['courses'] = courses
        return context
    
    
def students_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            return redirect('student_details', student_id = student.id)
    else:
        form = StudentForm()
    return render(request, 'course/students_create.html', {'form': form})

class StudentCreateNew(LoginRequiredMixin,CreateView):
    model = Student
    fields = ['name', 'address', 'phone_number', 'date_of_birth', 'gender', 'group', 'courses']
    template_name='course/groups_create.html'
    login_url = '/user/login/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



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

class StudentUpdateView(LoginRequiredMixin,UpdateView):
    model = Student
    fields = ['name', 'address', 'phone_number', 'date_of_birth', 'gender', 'group', 'courses']
    template_name = 'course/student_edit.html'
    pk_url_kwarg = 'student_id'
    login_url = '/user/login/'

def student_delete(request, student_id):
    query = Student.objects.get(pk=student_id)
    query.delete()
    return HttpResponseRedirect('/course/students')

class StudentDeleteView(LoginRequiredMixin,DeleteView):
    model = Student
    pk_url_kwarg = 'student_id'
    success_url = reverse_lazy('students_list')
    login_url = '/user/login/'

def student_random(request):
    students = Student.objects.all()
    random_student = random.choice(students)
    my_context = {'student': random_student}
    return render(request, 'course/student_detail.html', context=my_context)






















def courses_list(request):
    course = Course.objects.all()
    my_context = {'courses': course}
    return render(request, 'course/course-list.html', context = my_context)

class CourseListView(ListView):
    model = Course
    template_name = 'course/course-list.html'
    context_object_name = 'courses'

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {'courses': course}
    return render(request, 'course/course_details.html', context=context)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course/course_details.html'
    context_object_name = 'course'
    pk_url_kwarg = 'course_id'
    


@login_required
def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.creator = request.user
            course.save()
            return redirect('course_details', course_id=course.id)
    else:
        form = CourseForm()

    return render(request, 'course/course_create.html', {'form': form})

class CourseCreateView(LoginRequiredMixin,CreateView):
    model = Course
    fields = ['name']
    template_name='course/course_create.html'
    login_url = '/user/login/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())




def course_edit(request, course_id):
    course = get_object_or_404(Branch, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)    
        if form.is_valid():
            course = form.save()
            return redirect('course_details', course_id=course.id)
    else:
        form = CourseForm(instance=course)
    return render(request, 'course/course_edit.html', {'form': form})


class CourseUpdateView(LoginRequiredMixin,UpdateView):
    model = Course
    fields = ['name']
    template_name = 'course/course_edit.html'
    pk_url_kwarg = 'course_id'
    login_url = '/user/login/'

def course_delete(request, course_id):
    query = Course.objects.get(pk=course_id)
    query.delete()
    return HttpResponseRedirect("/course/course/")

class CourseDeleteView(LoginRequiredMixin,DeleteView):
    model = Course
    pk_url_kwarg = 'course_id'
    success_url = reverse_lazy('course_list')
    login_url = '/user/login/'

def course_random(request):
    courses = Course.objects.all()
    random_course = random.choice(courses)
    my_context = {'course': random_course}
    return render(request, 'course/course_details.html', context=my_context)











class BranchAPIView(APIView):
    
    def get(self, request, format = None):
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    
    def post(self, request):
        # Create an article from the above data
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            branch_saved = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GroupAPIView(APIView):
    
    def get(self, request, format = None):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)


class StudentAPIView(APIView):
    
    def get(self, request, format = None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
