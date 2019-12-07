from django.urls import path

from .import views

app_name = "offer"

urlpatterns = [
    path('', views.offer, name='offer'),
    path('save/', views.offer_save, name='offer_save'),
    path('list', views.OfferListView.as_view(), name='offer_list'),
    path('detail/<int:pk>/', views.OfferDetailView.as_view(), name='offer_list_detail'),
]
