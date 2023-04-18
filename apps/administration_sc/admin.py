from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(estudianteModel)
class studenAdmin(admin.ModelAdmin):
    pass
@admin.register(profesorModel)
class teacherAdmin(admin.ModelAdmin):
    pass
@admin.register(cursoModel)
class cursoAdmin(admin.ModelAdmin):
    pass
    



    
    


