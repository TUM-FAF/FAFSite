# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Rename field 'FAFUser.name'
        db.rename_column('general_fafuser', 'name', 'first_name')

        # Rename field 'FAFUser.surname'
        db.rename_column('general_fafuser', 'surname', 'last_name')

        # Deleting field 'FAFUser.email'
        db.delete_column(u'general_fafuser', 'email')


    def backwards(self, orm):
        # Rename field 'FAFUser.name'
        db.rename_column('general_fafuser', 'first_name', 'name')

        # Rename field 'FAFUser.surname'
        db.rename_column('general_fafuser', 'last_name', 'surname')

        # Adding field 'FAFUser.email'
        db.add_column(u'general_fafuser', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75),
                      keep_default=False)


    models = {
        u'general.fafuser': {
            'Meta': {'object_name': 'FAFUser'},
            'auth_user_id': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'general.usermeta': {
            'Meta': {'object_name': 'UserMeta'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.UserMetaType']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['general.FAFUser']"}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        u'general.usermetatype': {
            'Meta': {'object_name': 'UserMetaType'},
            'data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            'multiple': ('django.db.models.fields.BooleanField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '31'})
        }
    }

    complete_apps = ['general']
