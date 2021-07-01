
from course.models import Branch, Course
from django.db.models import base
from django.urls import path
from .views import BranchCreateView, BranchDeleteView, BranchDetailView, BranchListView, BranchUpdateView, CourseCreateView, CourseDeleteView, CourseDetailView, CourseListView, CourseUpdateView, GroupCreateNew, GroupDeleteView, GroupDetailView, GroupListView, GroupUpdateNew, StudentCreateNew, StudentDeleteView, StudentDetailView, StudentListView, StudentUpdateView, branch_delete, branch_details, branch_edit, branch_random, branches_list, course_random, group_delete, group_details, group_edit, group_list, group_random, groups_create, my_main_page, student_delete, student_details, student_edit, student_list, student_random, students_create
from django.urls import path, include


urlpatterns=[
    path('', my_main_page, name = 'my_main_page'),
    path('branches/', BranchListView.as_view(), name = 'branches_list' ),
    path('branches/create', BranchCreateView.as_view(), name = 'branches_create'),
    path('branches/<int:branch_id>/', BranchDetailView.as_view()    , name = 'branch_details'),
    path('branches/<int:branch_id>/edit', BranchUpdateView.as_view(), name='branch_edit'),
    path('branches/<int:branch_id>/delete', BranchDeleteView.as_view(), name='branch_delete'),
    path("branches/random/", branch_random, name="branch_random"),




    path('groups/', GroupListView.as_view(), name = 'groups_list'),
    path('groups/create', GroupCreateNew.as_view(), name = 'groups_create'),
    path('groups/<int:group_id>/', GroupDetailView.as_view(), name ='group_details'),
    path('groups/<int:group_id>/edit', GroupUpdateNew.as_view(), name ='group_edit'),
    path('groups/<int:group_id>/delete', GroupDeleteView.as_view(), name ='group_delete'),
    path("groups/random/", group_random, name="group_random"),






    path('students/', StudentListView.as_view(), name='students_list'),
    path('student/<int:student_id>/', StudentDetailView.as_view(), name='student_details'),
    path('students/create', StudentCreateNew.as_view(), name = 'students_create'),
    path('student/<int:student_id>/edit', StudentUpdateView.as_view(), name='student_edit'),
    path('student/<int:student_id>/delete', StudentDeleteView.as_view(), name='student_delete'),
    path("students/random/", student_random, name="student_random"),


    path('api/', include('course.api.urls')),




    path('course/', CourseListView.as_view(), name='course_list'),
    path('course/<int:course_id>/', CourseDetailView.as_view(), name='course_details'),
    path('course/create/', CourseCreateView.as_view(), name = 'course_create'),
    path('course/<int:course_id>/edit', CourseUpdateView.as_view(), name='course_edit'),
    path('course/<int:course_id>/delete', CourseDeleteView.as_view(), name='course_delete'),
    path("course/random/", course_random, name="course_random"),
]