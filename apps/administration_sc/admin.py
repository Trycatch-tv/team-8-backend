from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(estudianteModel)
class studen_Admin(admin.ModelAdmin):
    pass
@admin.register(profesorModel)
class teacher_Admin(admin.ModelAdmin):
    pass
@admin.register(cursoModel)
class curso_Admin(admin.ModelAdmin):
    pass
    



    
    


