from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


# class UserProfileManager(BaseUserManager):
#     def create_user(self, phone_number, password=None, **extra_fields):
#         pass
#
#     def create_superuser(self, phone_number, password=None, **extra_fields):
#         pass


class UserProfile(AbstractBaseUser):
    phone_number = models.CharField(max_length=15, unique=True, null=False, blank=False)
    invite_code = models.CharField(max_length=6, unique=True, null=True, blank=True)
    inviter_code = models.CharField(max_length=6, null=True, blank=True)
    referrals = models.ManyToManyField('self', symmetrical=False, related_name='invited_by')

    # objects = UserProfileManager()

    USERNAME_FIELD = 'phone_number'

    # REQUIRED_FIELDS = []

    def __str__(self):
        return f"Пользователь {self.phone_number}"


class AuthenticationCode(models.Model):
    phone_number = models.CharField(max_length=15, unique=True, null=False, blank=False)
    code = models.CharField(max_length=4)
    expiration_time = models.DateTimeField(null=True)

    def __str__(self):
        return f"Код для {self.phone_number}"
