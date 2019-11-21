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
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
