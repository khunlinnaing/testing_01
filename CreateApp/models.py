from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    value = models.IntegerField(default=0)
    name = models.CharField(default='user', max_length=500)

    def __str__(self):
        return self.name

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userinfo')
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='roleinfo')
