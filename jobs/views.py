from newsletter.forms import NewsletterSubForm
from django.db.models.query_utils import Q
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Job
from .forms import filterJob

def jobListView(request):
    jobs=Job.objects.all()
    form=filterJob()
    sub_form=NewsletterSubForm()
    if request.POST:
        form=filterJob(request.POST or None)
        if form.is_valid():
            search_term=form.cleaned_data['search']
            print(search_term)
            jobs=Job.objects.filter(
                Q( title__icontains=search_term) | 
                Q(job_type=search_term) |
                Q(company_location__icontains=search_term)|
                Q(description__icontains=search_term)
                )

    return render(request,'job_list.html',{
        'jobs':jobs,
        'form':form,
        'sub_form':sub_form
    })

class JobDetailView(DetailView):
    model=Job
    slug_field='id'
    slug_url_kwarg='id'
    template_name='job_detail.html'
    context_object_name='job'
    

    
