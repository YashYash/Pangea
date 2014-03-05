# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Video'
        db.delete_table(u'charity_app_video')


        # Renaming column for 'Charity.video' to match new field type.
        db.rename_column(u'charity_app_charity', 'video_id', 'video')
        # Changing field 'Charity.video'
        db.alter_column(u'charity_app_charity', 'video', self.gf('django.db.models.fields.CharField')(max_length=2000))
        # Removing index on 'Charity', fields ['video']
        db.delete_index(u'charity_app_charity', ['video_id'])


    def backwards(self, orm):
        # Adding index on 'Charity', fields ['video']
        db.create_index(u'charity_app_charity', ['video_id'])

        # Adding model 'Video'
        db.create_table(u'charity_app_video', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video_url', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('posted', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'charity_app', ['Video'])


        # Renaming column for 'Charity.video' to match new field type.
        db.rename_column(u'charity_app_charity', 'video', 'video_id')
        # Changing field 'Charity.video'
        db.alter_column(u'charity_app_charity', 'video_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charity_app.Video']))

    models = {
        u'charity_app.charity': {
            'Meta': {'object_name': 'Charity'},
            'charity_url': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        }
    }

    complete_apps = ['charity_app']