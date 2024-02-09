from django.db import models
from apps.roles.users_roles.models import Users

# Create your models here.fr

class Student(Users):
    def __init__(self, username):
        super().__init__(username, role="estudiante")
        self.type_document = None
        self.number_document = None
        self.identificacion_name = None
        self.full_name = None
        self.email_unique = None
        self.phone = None
        self.departments = None
        self.password = None
        self.estudiante_info = None  # Información específica para el rol de estudiante
        
        