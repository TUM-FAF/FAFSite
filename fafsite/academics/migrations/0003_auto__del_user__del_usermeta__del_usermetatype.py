# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ('general', '0002_auto__add_usermeta__add_usermetatype__add_fafuser'),
    )

    def forwards(self, orm):
        pass

    def backwards(self, orm):
        pass

    models = {
        u'academics.course': {
            'Meta': {'object_name': 'Course'},
            'courseProject': ('django.db.models.fields.BooleanField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'labs': ('django.db.models.fields.BooleanField', [], {}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'literature': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'professors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['general.FAFUser']", 'symmetrical': 'False', 'blank': 'True'}),
            'semester': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'subject_en': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'subject_ro': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        u'general.fafuser': {
            'Meta': {'object_name': 'FAFUser'},
            'auth_user_id': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '31'})
        }
    }

    complete_apps = ['academics']
