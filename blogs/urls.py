from django.contrib import admin
from django.urls import path
from blogs import views

urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('category/<slug:url>', views.category, name="category"),
    path('comments/', views.comment, name="comment"),
    path('<slug:url>', views.blogpost, name="blogpost"),
]