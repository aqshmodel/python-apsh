from django.urls import path

from .import views

app_name = "notification"

urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.reply_save, name='reply_save'),
    path('apply_list/', views.ApplyListView.as_view(), name='apply_list'),
    path('detail/<int:pk>/', views.ApplyDetailView.as_view(), name='apply_list_detail')
]
