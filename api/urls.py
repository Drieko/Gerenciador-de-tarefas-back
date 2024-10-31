# 100% de fé
from . import views
from django.urls import path

urlpatterns = {
    path('api/', views.get_items, name='get_api'),
    path('api/create/', views.create_item, name='create_api'),
}