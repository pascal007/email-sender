from django.db import models
from django.utils.translation import gettext_lazy as _
from DataAccessLayer.BaseModel import BaseModel
from DataAccessLayer.utils import GENDER_CHOICE
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_user(self, email, first_name, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(
            email=email, first_name=first_name, **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, password, **other_fields):
        other_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, first_name, password, **other_fields)


class User(PermissionsMixin, AbstractBaseUser, BaseModel):
    
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150)
    password = models.CharField(max_length=128, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    EMAIL_FIELD = 'email'
    objects = CustomAccountManager()

    def __str__(self):
        return self.email
