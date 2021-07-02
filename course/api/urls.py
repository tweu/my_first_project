
from django.urls.conf import include
from course.api.views import BranchViewSet, CourseViewSet, GroupViewSet, StudentViewSet
from course.models import Branch
from course.api.serializers import BranchModelSerializer
from django.urls import path
from rest_framework import routers


router = routers.DefaultRouter()
router.register('branches', BranchViewSet)
router.register('groups', GroupViewSet)
router.register('students', StudentViewSet)
router.register('couse', CourseViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    # path('v1/branches/', BranchListView.as_view(), name = 'branches'),
    # path('v1/branches/<int:pk>/', BranchDetailView.as_view(), name='branch_detail'),
    # path('v1/groups/', GroupListView.as_view(), name = 'groups'),
    # path('v1/groups/<int:pk>/', GroupDetailView.as_view(), name='group_detail'),
    # path('v1/students/', StudentListView.as_view(), name = 'students'),
    # path('v1/students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
]