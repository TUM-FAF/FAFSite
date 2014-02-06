# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'blog_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=63)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('preview', self.gf('tinymce.models.HTMLField')()),
            ('content', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'blog', ['Article'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'blog_article')


    models = {
        u'blog.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'content': ('tinymce.models.HTMLField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preview': ('tinymce.models.HTMLField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        }
    }

    complete_apps = ['blog']