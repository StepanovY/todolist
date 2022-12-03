from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Модель "Пользователь". Наследуется от AbstractUser.
    """
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=150, blank=True, verbose_name='Фамилия')
    email = models.EmailField(blank=True, unique=True, verbose_name="email address")

    # password = models.CharField(verbose_name='Пароль', max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
