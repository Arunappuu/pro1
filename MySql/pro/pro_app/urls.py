from django.urls import path
from . import views

urlpatterns = [
    path('reg', views.reg, name='reg'),
    path('login', views.log, name='login'),
    path('', views.index, name='index'),

]






