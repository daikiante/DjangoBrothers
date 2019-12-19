from django.db import models

# ここから追加
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.mail import send_mail
from django.utils import timezone


class UserManager(BaseUserManager):
    """カスタムユーザーマネージャー"""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        # emailを必須にする
        if not email:
            raise ValueError('The given email must be set')
        # emailでuserモデルを作成
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user



class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル"""
    initial_point = 50000
    email = models.EmailField("メールアドレス", unique=True)
    point = models.PositiveIntegerField(default=initial_point)
    is_staff = models.BooleanField("is_staff", default=False)
    is_active = models.BooleanField("is_active", default=True)
    date_joined = models.DateTimeField("date_joined", default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = 'users'
