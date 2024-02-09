from django.db import models

from django.core.mail import send_mail
# Create your models here.
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from django.utils import timezone

from random import choices

class CodigoVerificacion(models.Model):
    email = models.CharField(max_length=100)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)
    verify = models.BooleanField(default=False)

    def __str__(self):
        return f'Código de verificación para {self.email} {self.id}'

    class Meta:
        app_label = 'confimation_email'  # Reemplaza 'confirmation_email' con el nombre real de tu aplicación



