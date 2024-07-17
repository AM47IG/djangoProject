from django.urls import path
from . import views


app_name = 'task2'

urlpatterns = [
    path('func/', views.func_views),
    path('class/', views.class_views.as_view())
]