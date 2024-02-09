from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

from .models import estudianteModel  # Asegúrate de importar el modelo estudianteModel desde tu app




class TuUsuarioBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user_id = request.user_id  # Obtener el user_id del JWT si lo has incluido en el payload
            if user_id:
                user = estudianteModel.objects.get(pk=user_id, email_unique=email)
            else:
                user = estudianteModel.objects.get(email_unique=email)
            if user.check_password(password):
                return user
        except estudianteModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return estudianteModel.objects.get(pk=user_id)
        except estudianteModel.DoesNotExist:
            return None

class JWTAuthenticationWithTuUsuario(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token['user_id']
        backend = TuUsuarioBackend()
        setattr(self, 'user_id', user_id)  # Añadir el user_id al objeto request para su uso posterior
        return backend.get_user(user_id)

"""
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import estudianteModel

class EstudianteJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        try:
            # Obtener el token JWT de la solicitud
            raw_token = self.get_raw_token(request)

            # Validar y descodificar el token JWT
            validated_token = self.get_validated_token(raw_token)

            # Obtener el usuario a partir del token
            user = self.get_user(validated_token)

            # Verificar si el usuario es un estudiante válido
            if not isinstance(user, estudianteModel):
                raise AuthenticationFailed("Usuario no es un estudiante válido.")

            # Devolver el usuario y el token
            return user, validated_token
        except AuthenticationFailed:
            return None

    def get_user(self, validated_token):
        user_id = validated_token['user_id']
        try:
            return estudianteModel.objects.get(pk=user_id)
        except estudianteModel.DoesNotExist:
            return None"""




