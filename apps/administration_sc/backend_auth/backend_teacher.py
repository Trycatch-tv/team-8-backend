from django.contrib.auth.backends import BaseBackend
from ..models import profesorModel
class TeacherBackend(BaseBackend):
    def authenticate_teacher(self, request, correo=None, contrasena=None):
        try:
            profesor = profesorModel.objects.get(correo=correo)
            if profesor.contrasena == contrasena:
                return profesor
        except profesorModel.DoesNotExist:
            return None

    def get_teacher(self, user_id):
        try:
            return profesorModel.objects.get(pk=user_id)
        except profesorModel.DoesNotExist:
            return None