from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('sdp',views.sundepart),
    path('dc',views.doctor),
    path('book', views.booking),
    path('rcp',views.reciept),
    path('log', views.login),
    path('sup', views.signup),


]