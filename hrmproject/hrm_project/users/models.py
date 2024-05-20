from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import DO_NOTHING


class User(AbstractUser):

    full_name = models.CharField(max_length=100)


