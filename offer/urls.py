from django.urls import path

from .import views

app_name = "offer"

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.offer, name='offer'),
    path('save/', views.offer_save, name='offer_save'),
]