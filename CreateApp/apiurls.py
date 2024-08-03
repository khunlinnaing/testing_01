from django.urls import path
from . import apiviews

urlpatterns = [
    path('', apiviews.index, name='Home Page'),
    path('/register', apiviews.register, name='Register'),
    path('/image', apiviews.upload_image, name='testing')
]
