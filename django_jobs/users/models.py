from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db.models.fields.files import ImageField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

READINESS=(
    ('open and looking','open and looking'),
    ('open but not looking', 'open but not looking'),
    ('not looking','not looking')
)

SENIORITY=(
    ('Beginner','Beginner'),
    ('Junior','Junior'),
    ('Mid level','Mid level'),
    ('Senior','Senior'),
    ('Lead','Lead'),
    ('Manager','Manager')
)



class CustomAccountManager(BaseUserManager):

    def create_user(self, email, password,name, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('You must provide a valid email')
        email = self.normalize_email(email)
        user = self.model(name=name, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, name, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=500,unique=True)
    username=models.CharField(max_length=300,blank=True,null=True)
    name = models.CharField(max_length=500)
    professional_title=models.CharField(max_length=300,blank=True,null=True)
    about=models.TextField(blank=True)
    profile_pic=models.ImageField(null=True,blank=True)
    location=models.CharField(max_length=300,blank=True,null=True)
    job_readiness=models.CharField(choices=READINESS,max_length=25,default=1)
    seniority=models.CharField(choices=SENIORITY,max_length=30)
    skills=models.ManyToManyField('Skill',blank=True)
    languages=models.ManyToManyField('Language',blank=True)
    experiences=models.ManyToManyField('Experience',blank=True)
    eductions=models.ManyToManyField('Education',blank=True)
    resume=models.FileField(null=True,blank=True)
    privacy=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_recruiter=models.BooleanField(default=False)
    start_date=models.DateTimeField(default=timezone.now)

    objects=CustomAccountManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    name=models.CharField(max_length=255)

    def save(self,*args,**kwargs) -> None:
        self.name=f'#{self.name.lower()}'
        return super().save(*args,**kwargs)

    def __str__(self) -> str:
        return self.name


class Experience(models.Model):
    company=models.CharField(max_length=300)
    role=models.CharField(max_length=300)
    description=models.TextField()
    start_date=models.DateField()
    end_date=models.DateField(blank=True)
    until_now=models.BooleanField(default=False)


class Language(models.Model):
    name=models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name



class Education(models.Model):
    school=models.CharField(max_length=300)
    course=models.CharField(max_length=300)
    start_date=models.DateField()
    end_date=models.DateField(blank=True)
    until_now=models.BooleanField(default=False)
