from django import forms
from allauth.account.forms import SignupForm

class filterJob(forms.Form):
    search = forms.CharField(max_length=200)


class CustomSignupForm(SignupForm):
    name=forms.CharField(max_length=500)
    def save(self,request,*args, **kwargs):
        user=super().save(request)
        user.name=self.cleaned_data.get('name')
        return user

