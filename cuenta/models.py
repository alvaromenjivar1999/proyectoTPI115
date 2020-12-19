from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone



class gestionarCuenta(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Un usuario debe tener email en nuestra plataforma")

        usuario = self.model(
            email=self.normalize_email(email),
        )

        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, password):
        usuario = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        usuario.is_admin = True
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.save(using=self._db)
        return usuario


class Cuenta(AbstractBaseUser):
    nombre = models.CharField(verbose_name="nombre", max_length=30)
    apellido = models.CharField(verbose_name="apellido", max_length=30)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    fechaNacimiento = models.DateTimeField(verbose_name='fecha nacimiento', default=timezone.now)
    sexo = models.CharField(max_length=10, default='Femenino')
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = gestionarCuenta()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_Label):
        return True


