# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Item.cost'
        db.add_column(u'inventory_item', 'cost',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Item.cost'
        db.delete_column(u'inventory_item', 'cost')


    models = {
        u'inventory.item': {
            'Meta': {'object_name': 'Item'},
            'cost': ('django.db.models.fields.PositiveIntegerField', [], {}),
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