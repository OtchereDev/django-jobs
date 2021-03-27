from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import fields
from django.utils.translation import gettext_lazy as _
from django import forms
User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = ("email",)
        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserUpdateForm(forms.ModelForm):
    skills=forms.CharField( widget=forms.TextInput(attrs={'class': "form-control"}),required=False)
    
    languages=forms.CharField(required=False)
    class Meta:
        model=User
        fields=["name",
                "professional_title",
                "about",
                "profile_pic",
                "location",
                "job_readiness",
                "seniority",
                "resume",
                "privacy",
                "is_recruiter",]

    