from django.urls import path
from myapp import views

urlpatterns = [
    path('create_video/', views.create_video, name='create_video'),
]