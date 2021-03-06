from django.http.response import Http404
from rest_framework.views import APIView
from course.models import Branch, Course, Group, Student
from course.api.serializers import BranchModelSerializer, CourseModelSerializer, GroupModelSerializer, StudentModelSerilizer
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework import generics, mixins, viewsets, filters
from  rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend



class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchModelSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator = self.request.user)

    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'address']
    ordering_fields = ['name', 'address']
    ordering = ['-name']
    filterset_fields = ['name', 'address']



# class BranchListView(mixins.CreateModelMixin,
#                      mixins.ListModelMixin,
#                      generics.GenericAPIView):
#     queryset = Branch.objects.all()
#     serializer_class = BranchModelSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class BranchDetailView(mixins.DestroyModelMixin,
#                        mixins.UpdateModelMixin,
#                        mixins.RetrieveModelMixin,
#                        generics.GenericAPIView):
#     queryset = Branch.objects.all()
#     serializer_class = BranchModelSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



# class BranchListView(generics.ListCreateAPIView):
#     queryset = Branch.objects.all()
#     serializer_class = BranchModelSerializer


# class BranchDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Branch.objects.all()
#     serializer_class = BranchModelSerializer








class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator = self.request.user)

    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'branch']
    ordering_fields = ['name', 'branch']
    ordering = ['-name']
    filterset_fields = ['name', 'branch']





# class GroupListView(generics.ListCreateAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupModelSerializer


# class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupModelSerializer









# class GroupListView(mixins.CreateModelMixin,
#                      mixins.ListModelMixin,
#                      generics.GenericAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupModelSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class GroupDetailView(mixins.DestroyModelMixin,
#                        mixins.UpdateModelMixin,
#                        mixins.RetrieveModelMixin,
#                        generics.GenericAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupModelSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



# class GroupDetailAPIVIew(APIView):

#     def get_object(self, pk):
#         try:
#             group = Group.objects.get(pk=pk)
#             return group
#         except Group.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         group = self.get_object(pk)
#         serializer = GroupSerializer(group)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         group = self.get_object(pk)
#         serializer = GroupSerializer(instance=group, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         group = self.get_object(pk)
#         group.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)









class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerilizer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator = self.request.user)

    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'address', 'phone_number']
    ordering_fields = ['name', 'phone_number', 'address']
    ordering = ['-name']
    filterset_fields = ['name', 'address', 'phone_number']







# class StudentListView(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerilizer


# class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerilizer





# class StudentListView(mixins.CreateModelMixin,
#                      mixins.ListModelMixin,
#                      generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerilizer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class StudentDetailView(mixins.DestroyModelMixin,
#                        mixins.UpdateModelMixin,
#                        mixins.RetrieveModelMixin,
#                        generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentModelSerilizer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class StudentAPIView(APIView):
    
#     def get(self, request, format = None):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many = True)
#         return Response(serializer.data, status = status.HTTP_200_OK)

#     def post(self, request):
#         # Create an article from the above data
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             student_saved = serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)




# class StudentDetailAPIView(APIView):

#     def get_object(self, pk):
#         try:
#             student = Student.objects.get(pk=pk)
#             return student
#         except Student.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         student = self.get_object(pk)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         student = self.get_object(pk)
#         serializer = StudentSerializer(instance=student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         student = self.get_object(pk)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['-name']
    filterset_fields = ['name']



