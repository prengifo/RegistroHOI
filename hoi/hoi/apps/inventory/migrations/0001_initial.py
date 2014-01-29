# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'inventory_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'inventory', ['Item'])

        # Adding model 'ItemChange'
        db.create_table(u'inventory_itemchange', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Item'])),
            ('delta', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'inventory', ['ItemChange'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'inventory_item')

        # Deleting model 'ItemChange'
        db.delete_table(u'inventory_itemchange')


    models = {
        u'inventory.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'inventory.itemchange': {
            'Meta': {'object_name': 'ItemChange'},
            'delta': ('django.db.models.fields.IntegerField', [], {}),
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Item']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['inventory']