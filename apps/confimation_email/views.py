
from random import choices

from rest_framework import status

from django.template.loader import render_to_string

from rest_framework.response import Response



import smtplib
from email.message import EmailMessage
from random import choices
from django.http import HttpResponse

from os import path,getenv
from dotenv import load_dotenv

from pathlib import Path

from .models import CodigoVerificacion

# Create your views here.

from rest_framework.decorators import api_view


@api_view(['POST'])
def generar_codigo_verificacion(request,email):
    try:
        # Verificar si ya existe un correo en CodigoVerificacion
        if CodigoVerificacion.objects.filter(email=email).exists():
            # Aquí puedes decidir cómo manejar el caso cuando el correo ya existe
            # Puedes enviar una respuesta con un mensaje indicando que el correo ya está registrado
            return Response({'message': 'El correo ya está registrado', 'status': status.HTTP_409_CONFLICT}, status=status.HTTP_409_CONFLICT)
        
        # Si el correo no existe, continuar con la generación del código de verificación
        codigo = ''.join(choices('0123456789', k=6))
        model = CodigoVerificacion.objects.create(email=email, code=codigo)
    
    except Exception as e:
        return Response({'message': 'Error al procesar la solicitud', 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Datos para el envío del correo electrónico
    email_subject = 'Código de verificación'
    email_message = f'Tu código de verificación es: {codigo}'
    sender_email = str(getenv('EMAIL_HOST_USER'))  # Reemplaza con tu dirección de correo
    recipient_email = email  # Reemplaza con la dirección de correo del destinatario

    try:
        # Crear el objeto EmailMessage
        msg = EmailMessage()

        
        email_template = 'email_template.html'
        email_content = render_to_string(email_template, {'codigo_verificacion': codigo})

        # Configurar el correo electrónico
        msg = EmailMessage()
        msg['Subject'] = email_subject
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg.set_content(email_content,subtype="html")

        
        # Build paths inside the project like this: BASE_DIR / 'subdir'.
        BASE_DIR = Path(__file__).resolve().parent.parent

        load_dotenv()

        # Configurar la conexión al servidor SMTP
        smtp_server = str(getenv('EMAIL_HOST'))  # Reemplaza con la dirección de tu servidor SMTP
        smtp_port = str(getenv('EMAIL_PORT'))  # Reemplaza con el puerto adecuado de tu servidor SMTP
        smtp_username = str(getenv('EMAIL_HOST_USER'))  # Reemplaza con tu dirección de correo
        smtp_password = str(getenv('EMAIL_HOST_PASSWORD'))  # Reemplaza con tu contraseña de correo

        # Iniciar la conexión y enviar el correo
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)

        return Response({'message':'Correo enviado correctamente','status':status.HTTP_200_OK},status=status.HTTP_200_OK)
    except Exception as e:
        return  Response({'message':'Correo enviado correctamente','status':status.HTTP_404_NOT_FOUND},status=status.HTTP_404_NOT_FOUND)
        


@api_view(['POST'])
def verifyCodeEmail(request,email,code):
    model = CodigoVerificacion.objects.filter(email=email).first()  # Obtener el primer objeto o None si no existe
    if(model.code == code):
        model.delete()
        return Response({'message':'Codigo Validado Perfectamente','status':status.HTTP_200_OK},status=status.HTTP_200_OK)
    else:
        return Response({'message':'Codigo Incorrecto','status':status.HTTP_404_NOT_FOUNDT},status=status.HTTP_404_NOT_FOUND)
    
    


