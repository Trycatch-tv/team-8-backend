from django.contrib import admin

from .models import CodigoVerificacion
# Register your models here.

@admin.register(CodigoVerificacion)
class CodeVerifyAdmin(admin.ModelAdmin):
    pass