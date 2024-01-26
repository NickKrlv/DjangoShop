from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='image')
    phone = models.CharField(max_length=20, **NULLABLE, verbose_name='phone')
    country = models.CharField(max_length=20, **NULLABLE, verbose_name='country')
    email = models.EmailField(unique=True, verbose_name='email')
    email_token = models.CharField(max_length=50, **NULLABLE, verbose_name='email_token')
    is_active = models.BooleanField(default=False, verbose_name='is_active')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
