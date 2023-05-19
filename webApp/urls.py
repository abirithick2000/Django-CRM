from django.urls import path
from webApp import views

urlpatterns = [
    path('', views.home,name="home"),
    path('register/', views.register_user,name="register"),
    path('logout/', views.logout_user,name="logout")
]