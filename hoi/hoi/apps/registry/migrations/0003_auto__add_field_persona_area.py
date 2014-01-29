# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Persona.area'
        db.add_column(u'registry_persona', 'area',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Persona.area'
        db.delete_column(u'registry_persona', 'area')


    models = {
        u'registry.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'area': ('django.db.models.fields.IntegerField', [], {}),
            'contacto_emergencia': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'coordinador_docente': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'didentificacion': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'direccion_habitacion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'estado_civil': ('django.db.models.fields.IntegerField', [], {}),
            'estado_nacimiento': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'fecha_fin': ('django.db.models.fields.DateField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'hospital_procedencia': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'hospital_procedencia_direccion': ('django.db.models.fields.TextField', [], {}),
            'hospital_procedencia_telefono': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monografia': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'nombres': ('django.db.models.fields.DateField', [], {'max_length': '128'}),
            'nota_apreciativa': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_cadera': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_columna': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_definitiva': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_hombro': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_msis': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_no': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_od': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pais_nacimiento': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'parentesco_emergencia': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'sintesis_curricular': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'telefono_coordinador_docente': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'telefono_emergencia': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['registry']