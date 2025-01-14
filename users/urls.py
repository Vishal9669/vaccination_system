from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='register'),
    path('signin/', views.signin, name='login'),
]
