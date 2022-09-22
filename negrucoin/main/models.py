from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Client(models.Model):
    """Simple client model, that expands default User model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    money = models.DecimalField(max_digits=18, decimal_places=6, default=0)
    rubles = models.DecimalField(max_digits=9, decimal_places=2, default=0)
