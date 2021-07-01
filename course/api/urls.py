from django.urls import path
from .views import BranchAPIView, BranchDetailAPIView, GroupAPIView, GroupDetailAPIVIew, StudentAPIView, StudentDetailAPIView


urlpatterns = [
    path('v1/branches', BranchAPIView.as_view(), name = 'branches'),
    path('v1/branches/<int:pk>/', BranchDetailAPIView.as_view(), name='branch_detail'),
    path('v1/groups', GroupAPIView.as_view(), name = 'groups'),
    path('v1/groups/<int:pk>/', GroupDetailAPIVIew.as_view(), name='group_detail'),
    path('v1/students', StudentAPIView.as_view(), name = 'students'),
    path('v1/students/<int:pk>/', StudentDetailAPIView.as_view(), name='student_detail'),
]