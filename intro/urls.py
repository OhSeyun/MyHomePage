from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:msg_id>/', views.delete_message, name='delete_message'),
]
