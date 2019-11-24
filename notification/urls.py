from django.urls import path

from .import views

app_name = "notification"

urlpatterns = [
    path('', views.OfferListView.as_view(), name='offer_list'),
    path('detail/<int:pk>/', views.OfferDetailView.as_view(), name='offer_list_detail'),
]
