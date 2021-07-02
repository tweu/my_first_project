
from django.db.models.query import QuerySet
from course.models import Branch, Course, Group, Student
from django.http import request
from rest_framework import serializers


class BranchModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ('id', 'name', 'address', 'photo', 'creator',)


class GroupModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['branch'] = BranchModelSerializer(instance.branch).data
        data['course'] = CourseModelSerializer(instance.course).data
        return data



class StudentModelSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['group'] = GroupModelSerializer(instance.group).data
        return data


class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
















# class BranchSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(required = False)
#     address = serializers.CharField(required = True)
#     photo = serializers.ImageField(required = False)

#     def create(self, validated_data):
#         return Branch.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.address = validated_data.get('address', instance.address)
#         instance.photo = validated_data.get('photo', instance.photo)

#         instance.save()
#         return instance




# class GroupSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(required = False)
#     branch = serializers.PrimaryKeyRelatedField(required = True, queryset = Branch.objects.all())

#     def create(self, validated_data):
#         return Group.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.branch = validated_data.get('branch', instance.branch)

#         instance.save()
#         return instance




# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(required = False)
#     address = serializers.CharField(required = True)
#     phone_number = serializers.CharField(required = True)
#     date_of_birth = serializers.DateField(required = False)
#     gender = serializers.CharField(required = True)
#     group = serializers.PrimaryKeyRelatedField(required = False, queryset = Group.objects.all())

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.address = validated_data.get('address', instance.address)
#         instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
#         instance.gender = validated_data.get('gender', instance.gender)
#         instance.group = validated_data.get('group', instance.group)
#         instance.phone_number = validated_data.get('phone_number', instance.phone_number)

#         instance.save()
#         return instance


