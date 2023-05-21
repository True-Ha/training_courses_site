from django.contrib.auth.models import AbstractUser
from django.db import models


class IpModel(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class MyUser(AbstractUser):
    tele_name = models.CharField(max_length=250)
    tele_username = models.CharField(max_length=250)
    tele_user_id = models.CharField(max_length=250)
    email = models.EmailField(null=True, blank=True)
    payment = models.TextField(null=True, blank=True)
    has_payment = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.tele_name)


class Payment(models.Model):
    user_id = models.CharField(max_length=120, null=True, blank=True)
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_info = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return str(self.payment_info)
