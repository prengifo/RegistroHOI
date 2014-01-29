# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Persona'
        db.create_table(u'registry_persona', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('area', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')()),
            ('fecha_fin', self.gf('django.db.models.fields.DateField')()),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('didentificacion', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('nacionalidad', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('sexo', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')()),
            ('estado_nacimiento', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('pais_nacimiento', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('estado_civil', self.gf('django.db.models.fields.IntegerField')()),
            ('direccion_habitacion', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('telefonos', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('hospital_procedencia', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('hospital_procedencia_telefono', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('hospital_procedencia_direccion', self.gf('django.db.models.fields.TextField')()),
            ('coordinador_docente', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('telefono_coordinador_docente', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('email_coordinador_docente', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('contacto_emergencia', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('parentesco_emergencia', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('telefono_emergencia', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('nota_apreciativa', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('nota_cadera', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('nota_columna', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('nota_hombro', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('nota_msis', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('nota_no', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('nota_od', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('nota_apreciativa1', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('examen1', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('examen2', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('examen3', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('examen4', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('examen5', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('examen6', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('nota_apreciativa2', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('monografia', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('nota_mono', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('nota_definitiva', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('sintesis_curricular', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'registry', ['Persona'])


    def backwards(self, orm):
        # Deleting model 'Persona'
        db.delete_table(u'registry_persona')


    models = {
        u'registry.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'area': ('django.db.models.fields.IntegerField', [], {}),
            'contacto_emergencia': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'coordinador_docente': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'didentificacion': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'direccion_habitacion': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'email_coordinador_docente': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'estado_civil': ('django.db.models.fields.IntegerField', [], {}),
            'estado_nacimiento': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'examen1': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'examen2': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'examen3': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'examen4': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'examen5': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'examen6': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_fin': ('django.db.models.fields.DateField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'hospital_procedencia': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'hospital_procedencia_direccion': ('django.db.models.fields.TextField', [], {}),
            'hospital_procedencia_telefono': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monografia': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'nacionalidad': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'nota_apreciativa': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_apreciativa1': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_apreciativa2': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_cadera': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_columna': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_definitiva': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_hombro': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_mono': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_msis': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_no': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nota_od': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pais_nacimiento': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'parentesco_emergencia': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'sexo': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'sintesis_curricular': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'telefono_coordinador_docente': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'telefono_emergencia': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'telefonos': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['registry']