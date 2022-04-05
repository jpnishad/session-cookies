from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.setSession),
    path('get/', views.getSession),
    path('del/', views.delSession)
]
