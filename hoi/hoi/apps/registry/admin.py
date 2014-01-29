from django.contrib import admin
# from django.db.models import Count, Min, Sum, Avg
# from django import forms
from models import *


class PersonaAdmin(admin.ModelAdmin):
    search_fields = ['nombres', 'apellidos', 'didentificacion', 'hospital_procedencia']

admin.site.register(Persona, PersonaAdmin)
