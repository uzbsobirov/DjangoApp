from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class Register(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="Email", unique=True)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

    
    is_active = models.BooleanField(
        'is_active',
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_superuser = models.BooleanField(
        'superuser',
        default=False,
        help_text=_('Superuser can get access to admin page')
    )
    last_login = models.DateTimeField('last login', blank=True, null=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'full_name',
        'last_name',
        'password',
        'confirm_password',
        'is_staff',
        'is_superuser'
    ]

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email




    def info(self):
        return {
            'full_name': ('charfield', {
                'max_length': 100,
                'is_alpha': True,
                'is_empty': False
            }),
            'last_name': ('charfield', {
                'max_length': 100,
                'null': True,
                'is_alpha': True,
                'is_empty': True
            }),
            'email': ('emailfield', {
                'max_length': 100,
                'unique': True,
                'is_empty': False
            }),
            'password': ('charfield', {
                'max_length': 100,
                'alpha_numeric': True,
                'is_empty': False
            }),
            'confirm_password': ('charfield', {
                'max_length': 100,
                'alpha_numeric': True,
                'is_empty': False
            }),
            
        }