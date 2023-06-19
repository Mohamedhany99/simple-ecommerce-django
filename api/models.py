from django.db import models
from uuid import uuid4
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.
#customized user model
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(
        "username", max_length=150, unique=True, validators=[UnicodeUsernameValidator()]
    )
    email = models.EmailField("email", max_length=200, unique=True)
    password = models.CharField("password", max_length=128)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        db_table = "users"

class Profiler(models.Model): # the user class that extends the user built-in django model with onetoone field
    base_user = models.OneToOneField(
        User, verbose_name="base user", on_delete=models.RESTRICT
    )
    first_name = models.CharField(
        verbose_name="first name", max_length=20, null=True, blank=True
    )
    last_name = models.CharField(
        verbose_name="last name", max_length=20, null=True, blank=True
    )

    def __str__(self) -> str:
        return f"{self.first_name}"
    
    class Meta:
        verbose_name = "profiler"
        verbose_name_plural = "profiler"
        db_table = "profiler"