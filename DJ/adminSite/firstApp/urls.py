from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="home"),
    path('<slug:slug>/', views.LoginDetails, name="detail")
]