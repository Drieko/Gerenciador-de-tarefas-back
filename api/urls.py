# 100% de fé
from . import views
from django.urls import path

urlpatterns = {
    path('', views.get_items, name='get_api'),
    path('create/', views.create_item, name='create_api'),
}