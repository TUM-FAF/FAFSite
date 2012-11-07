# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('academics_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=31)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('academics', ['User'])

        # Adding model 'UserMetaType'
        db.create_table('academics_usermetatype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=31)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=31)),
            ('data', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('multiple', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('academics', ['UserMetaType'])

        # Adding model 'UserMeta'
        db.create_table('academics_usermeta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['academics.User'])),
            ('meta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['academics.UserMetaType'])),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('academics', ['UserMeta'])

        # Adding model 'Course'
        db.create_table('academics_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('subject_ro', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('subject_en', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('semester', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('courseProject', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('labs', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('literature', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('academics', ['Course'])

        # Adding M2M table for field professors on 'Course'
        db.create_table('academics_course_professors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm['academics.course'], null=False)),
            ('user', models.ForeignKey(orm['academics.user'], null=False))
        ))
        db.create_unique('academics_course_professors', ['course_id', 'user_id'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table('academics_user')

        # Deleting model 'UserMetaType'
        db.delete_table('academics_usermetatype')

        # Deleting model 'UserMeta'
        db.delete_table('academics_usermeta')

        # Deleting model 'Course'
        db.delete_table('academics_course')

        # Removing M2M table for field professors on 'Course'
        db.delete_table('academics_course_professors')


    models = {
        'academics.course': {
            'Meta': {'object_name': 'Course'},
            'courseProject': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'labs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'literature': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'professors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['academics.User']", 'symmetrical': 'False', 'blank': 'True'}),
            'semester': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'subject_en': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'subject_ro': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        'academics.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '31'})
        },
        'academics.usermeta': {
            'Meta': {'object_name': 'UserMeta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['academics.UserMetaType']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['academics.User']"}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        'academics.usermetatype': {
            'Meta': {'object_name': 'UserMetaType'},
            'data': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            'multiple': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '31'})
        }
    }

    complete_apps = ['academics']