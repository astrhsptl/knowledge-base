from django.db import models
from django.conf import settings 
from django.urls import reverse_lazy
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, PermissionsMixin
)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    DEPARTMENTS = (
        ('Коммерческий', 'Коммерческий'),
        ('Финансовый', 'Финансовый'),
        ('Маркетинговый', 'Маркетинговый'),
    )

    name = models.CharField(max_length=255,)
    middlename = models.CharField(max_length=255,)
    surname = models.CharField(max_length=255,)
    department = models.CharField(max_length=255, choices=DEPARTMENTS)
    email = models.EmailField(max_length=256, unique=True)
    private_access = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Auth settings
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self,):
        return reverse_lazy('user', kwargs={'pk': self.pk})