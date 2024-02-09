from django.db import models

from apps.roles.users_roles.models import Users

# Create your models here.
class profesorModel(Users):
    def __init__(self, username):
        super().__init__(username, role="profesor")
        self.nombre = None
        self.correo = None
        self.telefono = None
        self.descripcion = None
        self.area_especializacion = None
        self.estudiantes = None
        self.cursos = None
        self.created_at = None
        self.estado = None
        self.contrasena = None
        self.rol = None