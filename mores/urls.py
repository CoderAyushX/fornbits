from django.urls import path
from mores import views

urlpatterns = [
    path('', views.more, name="more"),
    path('editprofile/', views.editpro, name="editpro"),
    path('feedback/', views.feedback, name="feedback"),
    path('updates/', views.update, name="update"),
    path('rateus/', views.rateus, name="rateus"),
]