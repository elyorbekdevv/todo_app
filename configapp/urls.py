from . import views
from django.urls import path 

urlpatterns = [
    path('', views.hello, name='list'),
    path('update_task/<str:pk>/', views.updatetask, name='update_task'),
    path('delete/<str:pk>/', views.deletetask, name='delete')
]