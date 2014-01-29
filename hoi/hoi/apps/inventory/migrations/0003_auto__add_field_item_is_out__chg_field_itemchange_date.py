# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Item.is_out'
        db.add_column(u'inventory_item', 'is_out',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'ItemChange.date'
        db.alter_column(u'inventory_itemchange', 'date', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):
        # Deleting field 'Item.is_out'
        db.delete_column(u'inventory_item', 'is_out')


        # Changing field 'ItemChange.date'
        db.alter_column(u'inventory_itemchange', 'date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    models = {
        u'inventory.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_out': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'item_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'inventory.itemchange': {
            'Meta': {'object_name': 'ItemChange'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'delta': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Item']"})
        }
    }

    complete_apps = ['inventory']