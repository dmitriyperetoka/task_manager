from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Store custom users in the database."""

    full_name = models.CharField(max_length=200)
    first_name = None
    last_name = None
