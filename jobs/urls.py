from jobs.views import  JobDetailView, jobListView
from django.urls import path 

app_name='jobs'

urlpatterns = [
    path('all',jobListView,name='all_jobs'),
    path('<int:id>/',JobDetailView.as_view(),name='job_detail')
]
