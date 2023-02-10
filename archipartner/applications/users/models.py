from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    COMUNAS_CHILE = (
        ('Rancagua','Rancagua'),
        ('Valdivia','Valdivia'),
    )

    REGIONES_CHILE = (
        ('OHiggins','OHiggins'),
        ('BioBio','BioBio'),
        ('Los Ríos','Los Ríos')
    )

    PAISES = (
        ('Chile','Chile'),
        ('Colombia','Colombia'),
        ('Estados Unidos','Estados Unidos')
    )

    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    fono = models.CharField(max_length=10)
    dirección = models.CharField(max_length=30, blank=True)
    comuna = models.CharField(max_length=30, choices=COMUNAS_CHILE, blank=True)
    region = models.CharField(max_length=30, choices=REGIONES_CHILE, blank=True)
    pais = models.CharField(max_length=30, choices=PAISES, blank=True)
    codregistro = models.CharField(max_length=6, blank=True)
    ocupation = models.CharField(
        'Profesión',
        max_length=30, 
        blank=True
    )
    date_birth = models.DateField(
        'Fecha de nacimiento', 
        blank=True,
        null=True
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.nombres + ' ' +self.apellidos