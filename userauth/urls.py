from django.contrib import admin
from django.urls import path
from userauth import views

urlpatterns = [
    path('', views.nproflie, name="nproflie"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('edit-profile/', views.editProfile, name="editProfile"),
    path('logout/', views.logout , name="logout")

]