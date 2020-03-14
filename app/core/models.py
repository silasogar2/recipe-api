from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and safes a new user"""
        if not email:
            raise ValueError('Users must have email addresses') 
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user . set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creating and saving a new super user"""
        user = self.create_user(email, password)
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model that supports the use of username instead of email"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
 