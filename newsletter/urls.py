from newsletter.views import newletterSubView
from django.urls import path

app_name='newsletter'

urlpatterns = [
    path('subcribe',newletterSubView,name='subscribe')
]
