from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import LoginForm

from .import views

app_name = "registration"

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('regist/', views.regist, name='regist'),
    path('regist_save/', views.regist_save, name='regist_save'),
    path('role/', views.role, name='role'),
    path('recruiter/', views.recruiter, name='recruiter'),
    path('recruiter_save/', views.recruiter_save, name='recruiter_save'),
    path('jobseeker/', views.jobseeker, name='jobseeker'),
    path('jobseeker_save/', views.jobseeker_save, name='jobseeker_save'),
    path('desired_condition/', views.desired_condition, name='desired_condition'),
    path('desired_condition_save/', views.desired_condition_save, name='desired_condition_save'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
