from django.contrib.auth.models import AbstractUser
from rolepermissions.roles import AbstractUserRole
from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Employer(AbstractUser):
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    groups = models.ManyToManyField(
        Group,
        related_name='employer_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='employer_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Poste(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='postes')

    def __str__(self):
        return self.title
