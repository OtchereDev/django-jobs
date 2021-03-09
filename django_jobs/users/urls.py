from django.urls import path

from django_jobs.users.views import (
    userDetailView, user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path('profile/',userDetailView,name='profile'),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:email>/", view=user_detail_view, name="detail"),
    
]
