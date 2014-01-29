# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ItemChange.end'
        db.delete_column(u'inventory_itemchange', 'end')

        # Deleting field 'ItemChange.start'
        db.delete_column(u'inventory_itemchange', 'start')

        # Adding field 'ItemChange.date'
        db.add_column(u'inventory_itemchange', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 7, 25, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ItemChange.end'
        db.add_column(u'inventory_itemchange', 'end',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ItemChange.start'
        db.add_column(u'inventory_itemchange', 'start',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'ItemChange.date'
        db.delete_column(u'inventory_itemchange', 'date')


    models = {
        u'inventory.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'inventory.itemchange': {
            'Meta': {'object_name': 'ItemChange'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'delta': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Item']"})
        }
    }

    complete_apps = ['inventory']