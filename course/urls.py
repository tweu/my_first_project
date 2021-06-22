from django.db.models import base
from django.urls import path
from .views import BranchCreateView, BranchDeleteView, BranchDetailView, BranchListView, BranchUpdateView, GroupCreateNew, GroupDeleteView, GroupDetailView, GroupListView, GroupUpdateNew, StudentCreateNew, StudentDeleteView, StudentDetailView, StudentListView, StudentUpdateView, branch_delete, branch_details, branch_edit, branches_create, branches_list, group_delete, group_details, group_edit, group_list, groups_create, my_main_page, student_delete, student_details, student_edit, student_list, students_create

urlpatterns=[
    path('', my_main_page, name = 'my_main_page'),
    path('branches/', BranchListView.as_view(), name = 'branches_list' ),
    path('branches/create', BranchCreateView.as_view(), name = 'branches_create'),
    path('branches/<int:branch_id>/', BranchDetailView.as_view()    , name = 'branch_details'),
    path('branches/<int:branch_id>/edit', BranchUpdateView.as_view(), name='branch_edit'),
    path('branches/<int:branch_id>/delete', BranchDeleteView.as_view(), name='branch_delete'),





    path('groups/', GroupListView.as_view(), name = 'groups_list'),
    path('groups/create', GroupCreateNew.as_view(), name = 'groups_create'),
    path('groups/<int:group_id>/', GroupDetailView.as_view(), name ='group_details'),
    path('groups/<int:group_id>/edit', GroupUpdateNew.as_view(), name ='group_edit'),
    path('groups/<int:group_id>/delete', GroupDeleteView.as_view(), name ='group_delete'),





    path('students/', StudentListView.as_view(), name='students_list'),
    path('student/<int:student_id>/', StudentDetailView.as_view(), name='student_details'),
    path('students/create', StudentCreateNew.as_view(), name = 'students_create'),
    path('student/<int:student_id>/edit', StudentUpdateView.as_view(), name='student_edit'),
    path('student/<int:student_id>/delete', StudentDeleteView.as_view(), name='student_delete'),
]