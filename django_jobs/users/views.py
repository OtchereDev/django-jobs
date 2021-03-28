from django_jobs.users.models import Education, Experience
import json
from django.http.response import HttpResponse, HttpResponseBadRequest
from django_jobs.users.forms import UserUpdateForm
from typing import Optional
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views import View
from datetime import date
from django.contrib import messages
User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    # slug_field = "email"
    # slug_url_kwarg = "email"

    def get_object(self) -> models.Model:
        user=self.request.user
        print(user)
        return user
        # return super().get_object(queryset=queryset)
    
  

@login_required
def userDetailView(request):
    user=get_object_or_404(User,email=request.user.email)
    print(user)
    return render(request,'users/user_detail.html',{
        'object':user
    })



user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["name","email","professional_title",
                "about",
                "profile_pic",
                "location",
                "job_readiness",
                "seniority",
                "skills",
                "languages",
                "experiences",
                "resume",
                "privacy",
                "is_recruiter",]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return reverse("users:detail", kwargs={"email": self.request.user.email})

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"email": self.request.user.email})


user_redirect_view = UserRedirectView.as_view()


class UsersUpdateView(LoginRequiredMixin, SuccessMessageMixin, View):
    def get(self,request,*args, **kwargs):
    
        form=UserUpdateForm(instance=request.user)

        return render(request,"users/account_change_page.html",{
            "form":form
        })

    def post(self,request,*args, **kwargs):
        form=UserUpdateForm(request.POST,request.FILES,instance=request.user)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Profile Update')
           
        if  not form.is_valid():
           
            messages.add_message(request, messages.WARNING, 'Sorry Your Profile could not be updated')
            
            return render(request,"users/account_change_page.html",{
            "form":form
            })

        return render(request,"users/account_change_page.html",{
            "form":form
        })

class AddEductaion(LoginRequiredMixin,View):
    def post(self,request,*args, **kwargs):
        
        data=json.loads(request.body)
       
        new_education=Education.objects.create(**data)

        request.user.educations.add(new_education)
        
        return HttpResponse('okay')

class AddExperience(LoginRequiredMixin,View):
    def post(self,request,*args, **kwargs):
        
        data=json.loads(request.body)
       
        new_experience=Experience.objects.create(**data)
        print(new_experience)
        request.user.experiences.add(new_experience)
        
        return HttpResponse('okay')