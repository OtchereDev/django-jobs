from django_jobs.users.models import SENIORITY
from django.db import models
from django.utils.text import slugify

JOB_TYPE=(
    ('remote','remote'),
    ('remote-only','remote-only'),
    ('not-remote','not-remote'),
)

class Job(models.Model):
    company_name=models.CharField(max_length=500)
    company_logo=models.ImageField(null=True, blank=True)
    title=models.CharField(max_length=300)
    company_website=models.URLField(max_length=500,null=True,blank=True)
    company_location=models.CharField(max_length=200)
    job_type=models.CharField(max_length=20,choices=JOB_TYPE)
    slug=models.SlugField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    level=models.CharField(choices=SENIORITY,max_length=30)
    description=models.TextField(blank=True)
    tag=models.ManyToManyField('Tag',blank=True)
    how_to_apply=models.CharField(max_length=200)
    target=models.CharField(max_length=500)
    currency=models.CharField(max_length=200,blank=True,null=True)
    min_salary=models.PositiveIntegerField(blank=True,null=True)
    max_salary=models.PositiveIntegerField(blank=True,null=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        return super().save(*args,**kwargs)

class Company(models.Model):
    company_name=models.CharField(max_length=500)
    company_logo=models.ImageField(null=True, blank=True)
    company_website=models.URLField(max_length=500,null=True,blank=True)
    company_location=models.CharField(max_length=200)
    description=models.TextField(blank=True)

class Tag(models.Model):
    name=models.CharField(max_length=100)

    def save(self,*args,**kwargs):
        self.name=f'#{self.name.lower()}'
        return super().save(*args,**kwargs)