
from django.db import models
from django.db.models import manager
from django.db.models.manager import Manager


# Create your models here.

class Branch(models.Model):
    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'


    name = models.CharField(max_length=100, null = False)
    address = models.CharField(max_length=300, null = True)


    def __str__(self):
        return self.name

class Group(models.Model):
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
    

    name = models.CharField(max_length=100, null = False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):

    FEMALE = 'female'
    MALE = 'male'
    
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    
    )
    
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=300, null = True, blank=True) 
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=7, default=MALE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name



class Worker(models.Model):
    ANAS = 'Anas'
    KAIRAT = 'Kairat'
    
    MANAGERS = (
        (ANAS, 'Anas'),
        (KAIRAT, 'Kairat')
    )

    class Meta:
        verbose_name = 'Рабочий'
        verbose_name_plural = 'Рабочие'


    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    managers = models.CharField(choices=MANAGERS, max_length=8)
