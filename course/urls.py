from django.db.models import base
from django.urls import path
from .views import branch_details, branch_edit, branches_create, branches_list, group_details, group_edit, group_list, groups_create, my_main_page, student_details, student_edit, student_list, students_create

urlpatterns=[
    path('', my_main_page, name = 'my_main_page'),
    path('branches/', branches_list, name = 'branches_list' ),
    path('branches/create', branches_create, name = 'branches_create'),
    path('branches/<int:branch_id>/', branch_details, name = 'branch_details'),
    path('branches/<int:branch_id>/edit', branch_edit, name='branch_edit'),
    path('groups/', group_list, name = 'groups_list'),
    path('groups/create', groups_create, name = 'groups_create'),
    path('groups/<int:group_id>/', group_details, name ='group_details'),
    path('groups/<int:group_id>/edit', group_edit, name ='group_edit'),
    path('students/', student_list, name='students_list'),
    path('student/<int:student_id>/', student_details, name='student_details'),
    path('students/create', students_create, name = 'students_create'),
    path('student/<int:student_id>/edit', student_edit, name='student_edit'),
]