from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='Home Page'),
    path('login/', views.CustomLogin, name='login'),
    path('logout/', views.CustomLogOut, name='logout'),
    path('register', views.register, name='Register')
]
