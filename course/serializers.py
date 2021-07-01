
# from course.models import Branch
# from django.http import request
# from rest_framework import serializers


# class BranchSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(required = False)
#     address = serializers.CharField(required = True)
#     photo = serializers.ImageField(required = False)

#     def create(self, validated_data):
#         return Branch.objects.create(**validated_data)



# class GroupSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(required = False)
#     branch = serializers.CharField(required = True)
#     photo = serializers.ImageField(required = False)



# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(required = False)
#     address = serializers.CharField(required = True)
#     phone_number = serializers.CharField(required = True)
#     date_of_birth = serializers.DateField(required = True)
#     gender = serializers.CharField(required = True)
#     group = serializers.CharField(required = True)
#     courses = serializers.CharField(required = True)

