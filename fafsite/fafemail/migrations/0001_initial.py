# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'Email'
        db.create_table('fafemail_email', (
            ('id',
             self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=31,
                                                                  blank=True)),
            ('email',
             self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('fafemail', ['Email'])


    def backwards(self, orm):
        # Deleting model 'Email'
        db.delete_table('fafemail_email')


    models = {
        'fafemail.email': {
            'Meta': {'object_name': 'Email'},
            'email': (
            'django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': (
            'django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [],
                     {'max_length': '31', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['fafemail']