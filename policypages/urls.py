from django.contrib import admin
from django.urls import path
from policypages import views

urlpatterns = [
    path('', views.policy , name="policy"),
    path('privacypolicy/', views.privacypolicy , name="privacyupolicy"),
    path('terms/', views.terms , name="terms"),
    path('disclaimer/', views.disclaimer , name="disclaimer"),
    path('aboutus/', views.aboutus , name="aboutus"),
]