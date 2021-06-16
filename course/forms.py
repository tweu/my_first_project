
from django import forms
from django.forms import fields
from course.models import Branch, Group, Student


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('name', 'address')

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'branch')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'address', 'phone_number', 'gender', 'group', 'date_of_birth')