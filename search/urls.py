from django.urls import path
from .import views

app_name = "search"

urlpatterns = [
    path('', views.UserListView.as_view(), name='job_seekers_list'),
    path('detail/<int:pk>/', views.UserDetailView.as_view(), name='job_seekers_detail'),
]