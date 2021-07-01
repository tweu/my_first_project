from django.http.response import Http404
from rest_framework.views import APIView
from course.models import Branch, Group, Student
from course.api.serializers import BranchSerializer, GroupSerializer, StudentSerializer
from rest_framework import serializers, status
from rest_framework.response import Response


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







class BranchDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            branch = Branch.objects.get(pk=pk)
            return branch
        except Branch.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        branch = self.get_object(pk)
        serializer = BranchSerializer(branch)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        branch = self.get_object(pk)
        serializer = BranchSerializer(instance=branch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        branch = self.get_object(pk)
        branch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








class GroupAPIView(APIView):
    
    def get(self, request, format = None):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        # Create an article from the above data
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            group_saved = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)




class GroupDetailAPIVIew(APIView):

    def get_object(self, pk):
        try:
            group = Group.objects.get(pk=pk)
            return group
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = GroupSerializer(instance=group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        group = self.get_object(pk)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentAPIView(APIView):
    
    def get(self, request, format = None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        # Create an article from the above data
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            student_saved = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)




class StudentDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            student = Student.objects.get(pk=pk)
            return student
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
