from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('new/', views.new_Item, name='new_Item'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]