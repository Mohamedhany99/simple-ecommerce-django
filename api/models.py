from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.
#customized user model


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
