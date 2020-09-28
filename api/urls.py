from django.urls import path
from . import views

urlpatterns = [
    path('ServiceProvider/', views.ServiceProviders.as_view()),
    path('Client/', views.client.as_view())
]
