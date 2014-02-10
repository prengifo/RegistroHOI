from django.db import models
from django import forms

from django.contrib.admin.widgets import AdminDateWidget
from django.core.exceptions import ValidationError

# FINE ECHEMOS CODIGO EN ESPANOl.

ESTADO_CIVIL_CHOICES = (
    (0, 'Soltero'),
    (1, 'Casado'),
    (2, 'Divorciado'),
    (3, 'Viudo')
)

TIPOS = (
    (0, 'Pasantia'),
    (1, 'Post-Grado'),
    (2, 'Fellow'),
    (3, 'Visitor')
)

AREAS = (
    (0, u'Ortopedia Infantil'),
    (1, u'Hombro'),
    (2, u'Columna'),
    (3, u'Cadera'),
    (4, u'Miembros inferiores'),
    (5, u'Neuro-Ortopedia'),
    (6, u'Medicina fisica y rehabilitacion'),
    (7, u'Cirugia de mano'),
    (8, u'Pediatria'),
    (9, u'Fisioterapia'),
    (10, u'Terapia del Lenguaje'),
    (11, u'Taller de Ortopedia'),
    (12, u'Terapia Ocupacional'),
)

SEX_CHOICES = (
    (0, 'Femenino'),
    (1, 'Masculino')
)



def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 1.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Tamano maximo es %sMB" % str(megabyte_limit))


class Persona(models.Model):
    
    tipo = models.IntegerField(choices=TIPOS)
    area = models.IntegerField(choices=AREAS)
    # Datos del semestre
    fecha_inicio = models.DateField('inicio periodo')
    fecha_fin = models.DateField('fin periodo')

    foto = models.ImageField('foto', upload_to='fotos/',validators=[validate_image], null=True, blank=True)

    # Datos de la persoan
    apellidos = models.CharField('apellidos', max_length=128)
    nombres = models.CharField('nombres', max_length=128)
    didentificacion = models.CharField('documento de identificacion', max_length=64)
    nacionalidad = models.CharField('nacionalidad', max_length=64)
    sexo = models.PositiveIntegerField('sexo', choices=SEX_CHOICES)
    fecha_nacimiento = models.DateField('fecha de nacimiento')
    estado_nacimiento = models.CharField('estado de nacimiento', max_length=64)
    pais_nacimiento = models.CharField('pais de nacimiento', max_length=64)
    estado_civil = models.IntegerField('estado civil', choices=ESTADO_CIVIL_CHOICES)
    direccion_habitacion = models.TextField('direccion de habitacion')
    email = models.EmailField('email', blank=True, null=True)
    telefonos = models.CharField('telefonos', max_length=64)

    # Hospital de procedencia
    hospital_procedencia = models.CharField('hospital/Instituo de procedencia', max_length=64)
    hospital_procedencia_telefono = models.CharField('telefono Hospital/Instituto de procedencia', max_length=64, blank=True, null=True)
    hospital_procedencia_direccion = models.TextField('direccion Hospital/Instituto de procedencia')
    coordinador_docente = models.CharField('coordinador docente Hospital/Instituto de precedencia', max_length=64)
    telefono_coordinador_docente = models.CharField('telefono coordinador docente Hospital/Instituto', max_length=64)
    email_coordinador_docente = models.EmailField('email coordinador docente', blank=True, null=True)

    # contacto de emergencia
    contacto_emergencia = models.CharField('persona contacto en caso de emergencia', max_length=64)
    parentesco_emergencia = models.CharField('parentesco persona contacto en caso de emergencia', max_length=64)
    telefono_emergencia = models.CharField('telefono de emergencia', help_text="en caso de emergencia llamar a este numero", max_length=64)

    # notas
    nota_apreciativa = models.PositiveSmallIntegerField('nota apreciativa', blank=True, null=True)
    nota_cadera = models.PositiveSmallIntegerField('nota cadera (Cad)', blank=True, null=True)
    nota_columna = models.PositiveSmallIntegerField('nota columna (Col)', blank=True, null=True)
    nota_hombro = models.PositiveSmallIntegerField('nota hombro (Hom)', blank=True, null=True)
    nota_msis = models.PositiveSmallIntegerField('nota miembros inferiores (msis)', blank=True, null=True)
    nota_no = models.PositiveSmallIntegerField('nota NO', blank=True, null=True)
    nota_od = models.PositiveSmallIntegerField('nota OD', blank=True, null=True)
    nota_apreciativa1 = models.PositiveSmallIntegerField('nota apreciativa examenes', blank=True, null=True)
    examen1 = models.PositiveSmallIntegerField('examen 1', blank=True, null=True)
    examen2 = models.PositiveSmallIntegerField('examen 2', blank=True, null=True)
    examen3 = models.PositiveSmallIntegerField('examen 3', blank=True, null=True)
    examen4 = models.PositiveSmallIntegerField('examen 4', blank=True, null=True)
    examen5 = models.PositiveSmallIntegerField('examen 5', blank=True, null=True)
    examen6 = models.PositiveSmallIntegerField('examen 6', blank=True, null=True)
    nota_apreciativa2 = models.PositiveSmallIntegerField('nota apreciativa monografia', blank=True, null=True)
    monografia = models.CharField('titulo de monografia', max_length=128, blank=True, null=True)
    nota_mono = models.PositiveSmallIntegerField('nota monografia', blank=True, null=True)
    nota_definitiva = models.PositiveSmallIntegerField('nota definitiva', blank=True, null=True)

    amonestaciones = models.PositiveSmallIntegerField('amonestaciones',blank=True,null =True)

    sintesis_curricular = models.TextField('sintesis curricular', help_text='solo necesario en caso de ser postgrado', blank=True, null=True)

    # datos de aprobacion
    # TODO: lugar_aprobacion, fecha_aprobacion?

    @property
    def edad(self):
        from datetime import date
        today = date.today()
        x = today-self.fecha_nacimiento
        return int(x.days/365.2425)

    @property
    def lugar_nacimiento(self):
        return '%s, %s' % (self.estado_nacimiento, self.pais_nacimiento)

REPORTES = (
    (1, 'Programa'),
    (2, 'Area'),
    (3, 'Pais'),
    (4, 'Genero')
)

class JQueryUIDatepickerWidget(forms.DateInput):
    def __init__(self, **kwargs):
        super(forms.DateInput, self).__init__(attrs={"size":10, "class": "dateinput"}, **kwargs)

    class Media:
        css = {"all":("http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.6/themes/redmond/jquery-ui.css",)}
        js = ("http://ajax.googleapis.com/ajax/libs/jquery/1.4.3/jquery.min.js",
              "http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.6/jquery-ui.min.js",)

class Report(forms.Form):
    tipo = forms.ChoiceField(choices=REPORTES)
    pinicio = forms.DateField(label='Fecha de Inicio del reporte', widget=JQueryUIDatepickerWidget, input_formats=['%d/%m/%Y'])
    pfin = forms.DateField(label='Fecha Final del reporte', widget=JQueryUIDatepickerWidget, input_formats=['%d/%m/%Y'] )
