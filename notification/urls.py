from django.urls import path

from .import views

app_name = "notification"

urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.apply_save, name='apply_save'),
    path('apply_list/', views.ApplyListView.as_view(), name='apply_list'),
    path('detail/<int:pk>/', views.ApplyDetailView.as_view(), name='apply_list_detail'),
    path('hiring_save/', views.hiring_save, name='hiring_save'),
    path('hiring_list/', views.HiringListView.as_view(), name='hiring_list'),
]
