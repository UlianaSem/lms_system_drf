from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, unique=True, verbose_name='Почта')

    telephone = models.CharField(max_length=35, verbose_name="Номер телефона", **NULLABLE)
    city = models.CharField(max_length=150, verbose_name="Город", **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name="Фото", **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
