from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='auth_users',
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='auth_users',
        related_query_name='user',
    )

class WebsiteUser(User):
    class Meta:
        proxy = True

class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery')

WebsiteUser.groups.through.__str__ = lambda self: f"{self.user} belongs to {self.group}"

