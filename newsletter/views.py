from django.http.response import JsonResponse
from jobs.forms import filterJob
from jobs.models import Job
from newsletter.forms import NewsletterSubForm
from django.shortcuts import redirect, render

def newletterSubView(request):
    if request.POST:
        sub_form=NewsletterSubForm(request.POST or None)
        if sub_form.is_valid():
            email=sub_form.cleaned_data['email']
            print(email)
            
    return redirect('jobs:all_jobs')