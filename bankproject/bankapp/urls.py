from django.urls import path
from .import views
app_name='bankapp'

urlpatterns = [
   path('forms',views.forms,name='forms'),
   path('',views.demo,name='demo'),
   path('login', views.login, name='login'),



]