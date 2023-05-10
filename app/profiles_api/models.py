from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for custom user profiles"""
    # Define methods for custom manager to manipulate relevant models.
    def create_user(self, email, name, password=None):
        """Create a new user profile through Djnago CLI"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        # Ensure that password is stored  encrypted.
        user.set_password(password)
        # Django default db
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Required for Django command line tools to manage custom users.
    objects = UserProfileManager()

    # Overriding default username field for authentication.
    # Default authentication is based on username/password.
    USERNAME_FIELD = 'email'
    # Define additional required fields
    REQUIRED_FIELDS = ['name']

    # Reuqired for Django to interact with custom user model.
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    # Convert UserProfile object to a string.
    def __str__(self):
        """Returng string representation of our user"""
        return self.email
