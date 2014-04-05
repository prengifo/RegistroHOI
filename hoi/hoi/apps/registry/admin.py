from django.contrib import admin
# from django.db.models import Count, Min, Sum, Avg
# from django import forms
from models import *
from django.http import HttpResponse


class PersonaAdmin(admin.ModelAdmin):
    def export_csv(modeladmin, request, queryset):
        import csv
        from django.utils.encoding import smart_str
        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=DatosEstudiantes.csv'
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8'))
        writer.writerow([
            smart_str(u"Tipo"),
            smart_str(u"Area"),
            smart_str(u"Apellidos"),
            smart_str(u"Nombres"),
            smart_str(u"Documento Identificacion"),
            smart_str(u"Nacionalidad"),
            smart_str(u"Sexo"),
            smart_str(u"Fecha Inicio"),
            smart_str(u"Fecha Fin"),
            smart_str(u"Fecha Nacimiento"),
            smart_str(u"Estado Civil"),
            smart_str(u"Estado Nacimiento"),
            smart_str(u"Pais Nacimiento"),

        ])
        for obj in queryset:
            if obj.sexo == 0:
                sexo = 'Femenino'
            else:
                sexo ='Masculino'

            if obj.area == 0:
                area = 'Ortopedia Infantil'
            elif obj.area == 1:
                area = 'Hombro'
            elif obj.area == 2:
                area = 'Columna'
            elif obj.area == 3:
                area = 'Cadera'
            elif obj.area == 4:
                area = 'Miembros Inferiores'
            elif obj.area == 5:
                area = 'Neuro-Ortopedia'
            elif obj.area == 6:
                area = 'Medicina fisica y rehabilitacion'
            elif obj.area ==7:
                area = 'Cirugia de mano'
            elif obj.area == 8:
                area = 'Pediatria'
            elif obj.area == 9:
                area = 'Fisioterapia'
            elif obj.area == 10:
                area = 'Terapia del Lenguaje'
            elif obj.area == 11:
                area = 'Taller de Ortopedia'
            elif obj.area == 12:
                area = 'Terapia Ocupacional'

            if obj.tipo == 0:
                tipo ='Pasantia'
            elif obj.tipo == 1:
                'Post-Grado'
            elif obj.tipo == 2:
                'Fellow'
            elif obj.tipo == 3:
                'Visitor'

            if obj.estado_civil == 0:
                estado_civil ='Soltero'
            elif obj.estado_civil == 1:
                estado_civil = 'Casado'
            elif obj.estado_civil == 2:
                estado_civil= 'Divorciado'
            elif obj.estado_civil == 3:
                estado_civil= 'Viudo'

            writer.writerow([
                smart_str(tipo),
                smart_str(area),
                smart_str(obj.apellidos),
                smart_str(obj.nombres),
                smart_str(obj.didentificacion),
                smart_str(obj.nacionalidad),
                smart_str(sexo),
                smart_str(obj.fecha_inicio),
                smart_str(obj.fecha_fin),
                smart_str(estado_civil),
                smart_str(obj.estado_nacimiento),
                smart_str(obj.pais_nacimiento),
            ])
        return response
    export_csv.short_description = u"Descargar informacion formato CSV"


    def export_xls(modeladmin, request, queryset):
        import xlwt
        response = HttpResponse(mimetype='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=DatosEstudiantes.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet("Persona")

        row_num = 0

        columns = [
            (u"Tipo",2000),
            (u"Area",2000),
            (u"Apellidos",2500),
            (u"Nombres", 2000),
            (u"Documento Identificacion", 4000),
            (u"Nacionalidad", 3000),
            (u"Sexo", 2000),
            (u"Fecha Inicio", 2000),
            (u"Fecha Fin", 2000),
            (u"Fecha Nacimiento", 3000),
            (u"Estado Civil", 2000),
            (u"Estado Nacimiento", 3000),
            (u"Pais Nacimiento", 3000),
        ]

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        for col_num in xrange(len(columns)):
            ws.write(row_num, col_num, columns[col_num][0], font_style)
            # set column width
            ws.col(col_num).width = columns[col_num][1]

            font_style = xlwt.XFStyle()
            font_style.alignment.wrap = 1

        for obj in queryset:
            if obj.sexo == 0:
                sexo = 'Femenino'
            else:
                sexo ='Masculino'

            if obj.area == 0:
                area = 'Ortopedia Infantil'
            elif obj.area == 1:
                area = 'Hombro'
            elif obj.area == 2:
                area = 'Columna'
            elif obj.area == 3:
                area = 'Cadera'
            elif obj.area == 4:
                area = 'Miembros Inferiores'
            elif obj.area == 5:
                area = 'Neuro-Ortopedia'
            elif obj.area == 6:
                area = 'Medicina fisica y rehabilitacion'
            elif obj.area ==7:
                area = 'Cirugia de mano'
            elif obj.area == 8:
                area = 'Pediatria'
            elif obj.area == 9:
                area = 'Fisioterapia'
            elif obj.area == 10:
                area = 'Terapia del Lenguaje'
            elif obj.area == 11:
                area = 'Taller de Ortopedia'
            elif obj.area == 12:
                area = 'Terapia Ocupacional'

            if obj.tipo == 0:
                tipo ='Pasantia'
            elif obj.tipo == 1:
                'Post-Grado'
            elif obj.tipo == 2:
                'Fellow'
            elif obj.tipo == 3:
                'Visitor'

            if obj.estado_civil == 0:
                estado_civil ='Soltero'
            elif obj.estado_civil == 1:
                estado_civil = 'Casado'
            elif obj.estado_civil == 2:
                estado_civil= 'Divorciado'
            elif obj.estado_civil == 3:
                estado_civil= 'Viudo'

            row_num += 1
            row = [
                tipo,
                area,
                obj.apellidos,
                obj.nombres,
                obj.didentificacion,
                obj.nacionalidad,
                sexo,
                obj.fecha_inicio,
                obj.fecha_fin,
                obj.fecha_nacimiento,
                estado_civil,
                obj.estado_nacimiento,
                obj.pais_nacimiento
            ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response

    export_xls.short_description = u"Descargar informacion formato XLS"


    search_fields = ['nombres', 'apellidos', 'didentificacion', 'hospital_procedencia']

    actions = [export_csv]


admin.site.register(Persona, PersonaAdmin)
