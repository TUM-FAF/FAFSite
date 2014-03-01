# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.auth_user_id'
        db.add_column(u'academics_user', 'auth_user_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.auth_user_id'
        db.delete_column(u'academics_user', 'auth_user_id')


    models = {
        u'academics.course': {
            'Meta': {'object_name': 'Course'},
            'courseProject': ('django.db.models.fields.BooleanField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'labs': ('django.db.models.fields.BooleanField', [], {}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'literature': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'professors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['academics.User']", 'symmetrical': 'False', 'blank': 'True'}),
            'semester': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'subject_en': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'subject_ro': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        u'academics.user': {
            'Meta': {'object_name': 'User'},
            'auth_user_id': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '31'})
        },
        u'academics.usermeta': {
            'Meta': {'object_name': 'UserMeta'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['academics.UserMetaType']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['academics.User']"}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        u'academics.usermetatype': {
            'Meta': {'object_name': 'UserMetaType'},
            'data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            'multiple': ('django.db.models.fields.BooleanField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '31'})
        }
    }

    complete_apps = ['academics']