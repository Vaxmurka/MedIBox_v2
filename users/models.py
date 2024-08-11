from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    role = models.CharField(max_length=256, blank=True, null=True, verbose_name="Роль")
    telegram = models.CharField(max_length=100, blank=True, null=True, verbose_name='Telegram')
    password = models.CharField(max_length=256, blank=True, null=True, verbose_name='Пароль')

    class Meta:
        db_table = 'Users'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.telegram} - {self.username}'

    def get_role(self) -> int:
        if self.role:
            if self.role == '1':
                return 1
            elif self.role == '2':
                return 2
        else: return 0