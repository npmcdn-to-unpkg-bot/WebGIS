import uuid
from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

#class User(models.Model):
#    email = models.EmailField(primary_key=True)
#    REQUIRED_FIELDS = ()
#    USERNAME_FIELD = 'email'


class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(default=uuid.uuid4, max_length=40)


class DatasetUserManager(BaseUserManager):

    def create_user(self, email):
        DatasetUser.objects.create(email=email)

    def create_superuser(self, email, password):
        self.create_user(email)


class DatasetUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key=True)
    USERNAME_FIELD = 'email'

    objects = DatasetUserManager()

    @property
    def is_staff(self):
        return self.email == 'pat@example.com'

    @property
    def is_active(self):
        return True
