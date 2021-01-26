from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)
    phone = models.CharField(max_length=13 ,blank=True, null=True)
    address = models.CharField(max_length=200 ,blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self) -> str:
        return f'Profile for {self.user.first_name}'
