from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField
from django.utils.translation import gettext_lazy as _

from blau_backend.users.managers import CustomUserManager


class User(AbstractUser):
    """Default user for BLAU Backend."""

    username = None
    first_name = None
    last_name = None
    email = EmailField(
        _("email address"), max_length=255, unique=True, blank=False, null=False
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
