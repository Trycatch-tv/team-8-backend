from django.urls import path

from .views import generar_codigo_verificacion,verifyCodeEmail

urlpatterns = [
    path('email/generate-code/<str:email>',generar_codigo_verificacion,name="generate_email"),
    path('email/verify-code/<str:email>/<str:code>',verifyCodeEmail,name="code_verify"),
]
