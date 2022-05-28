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
    path('adp', views.amaladepart),
    path('edp', views.elitedepart),
    path('jdp', views.jubiliedepart),
    path('wdp', views.westfortdepart),
]