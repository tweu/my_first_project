from django.db.models import base
from django.urls import path
from .views import branch_details, branches_list, group_details, group_list, my_main_page, student_details, student_list

urlpatterns=[
    path('', my_main_page, name = 'my_main_page'),
    path('branches/', branches_list, name = 'branches_list' ),
    path('branches/<int:branch_id>/', branch_details, name = 'branch_details'),
    path('groups/', group_list, name = 'groups_list'),
    path('groups/<int:group_id>/', group_details, name ='group_details'),
    path('students/', student_list, name='students_list'),
    path('student/<int:student_id>/', student_details, name='student_details')
]