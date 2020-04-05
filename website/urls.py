
from django.urls import path
from . import views

urlpatterns = [
    path('home.html', views.home, name="home"),
    path('add.html', views.add, name="add"),
    path('soustract.html', views.soustract, name="soustract"),
    path('multiply.html', views.multiply, name="multiply"),
    path('division.html', views.division, name="division"),


]
