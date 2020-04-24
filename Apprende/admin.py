from django.contrib import admin
from .models import * #importamos el modelo
# Register your models here.
admin.site.register(Curso)  # Registramos la clase Curso
admin.site.register(Autor)  # Registramos la clase Autor
# admin.site.register(Unidad)  # Registramos la clase Unidad