from django.urls import path

from django_jobs.users.views import (
    userDetailView, user_detail_view,UsersUpdateView,AddEductaion,AddExperience,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path('profile/',user_detail_view,name='profile'),
    path('profile_update/',UsersUpdateView.as_view(),name='profile_update'),
    path('add_education/',AddEductaion.as_view(),name='add_education'),
    path('add_experience/',AddExperience.as_view(),name='add_experience'),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:email>/", view=user_detail_view, name="detail"),
    
]
