# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.contrib.contenttypes.models import ContentType


class Migration(SchemaMigration):

    def forwards(self, orm):

        db.rename_table('academics_user', 'general_fafuser')
        # db.rename_table('academics_user', 'general_user')
        db.rename_table('academics_usermeta', 'general_usermeta')
        db.rename_table('academics_usermetatype', 'general_usermetatype')

        db.rename_column('academics_course_professors', 'user_id', 'fafuser_id')
        # db.rename_column('general_usermeta', 'user_id', 'fafuser_id')

        if not db.dry_run:
            # For permissions to work properly after migrating
            ContentType.objects.filter(app_label='academics', model='user').update(app_label='general', model='fafuser')
            # ContentType.objects.filter(app_label='academics', model='user').update(app_label='general')
            ContentType.objects.filter(app_label='academics', model='usermeta').update(app_label='general')
            ContentType.objects.filter(app_label='academics', model='usermetatype').update(app_label='general')

    def backwards(self, orm):
        db.rename_table('general_fafuser', 'academics_user')
        # db.rename_table('general_user', 'academics_user')
        db.rename_table('general_usermeta', 'academics_usermeta')
        db.rename_table('general_usermetatype', 'academics_usermetatype')

        db.rename_column('academics_course_professors', 'fafuser_id', 'user_id')
        # db.rename_column('general_usermeta', 'fafuser_id', 'user_id')

        if not db.dry_run:
            # For permissions to work properly after migrating
            ContentType.objects.filter(app_label='general', model='fafuser').update(app_label='academics', model='user')
            # ContentType.objects.filter(app_label='general', model='user').update(app_label='academics')
            ContentType.objects.filter(app_label='general', model='usermeta').update(app_label='academics')
            ContentType.objects.filter(app_label='general', model='usermetatype').update(app_label='academics')

    models = {
        u'general.fafuser': {
            'Meta': {'object_name': 'FAFUser'},
            'auth_user_id': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '31'})
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
