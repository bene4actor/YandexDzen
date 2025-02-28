from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def _validate(self, **kwargs):
        missing_fields = [k for k, v in kwargs.items() if v is None]
        if missing_fields:
            raise ValueError(f"You have not entered: {', '.join(missing_fields)}")

    def _create(self, email: str, username: str, telegram_chat_id: str, password: str, **extra):
        self._validate(email=email, password=password)
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            telegram_chat_id=telegram_chat_id,
            **extra
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, username: str, telegram_chat_id: str, password: str, **extra):
        return self._create(
            email=email,
            username=username,
            telegram_chat_id=telegram_chat_id,
            password=password,
            is_active=True,
            **extra
        )

    def create_superuser(self, email: str, password: str):
        return self._create(email, password, is_staff=True, is_superuser=True, is_active=True)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name="Почта")
    username = models.CharField(max_length=255, null=True, blank=True, verbose_name="Имя")
    telegram_chat_id = models.CharField(max_length=255, null=True, blank=True, verbose_name="Телерам чат")

    is_active = models.BooleanField(default=False, verbose_name='Активный')
    is_banned = models.BooleanField(default=False, verbose_name='Заблокированный')
    is_staff = models.BooleanField(default=False, verbose_name='Персонал')
    is_superuser = models.BooleanField(default=False, verbose_name='Админ')

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'users'
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username or self.email