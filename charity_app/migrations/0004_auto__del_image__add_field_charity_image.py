# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Image'
        db.delete_table(u'charity_app_image')

        # Adding field 'Charity.image'
        db.add_column(u'charity_app_charity', 'image',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=2000),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Image'
        db.create_table(u'charity_app_image', (
            ('image_url', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('charity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['charity_app.Charity'])),
        ))
        db.send_create_signal(u'charity_app', ['Image'])

        # Deleting field 'Charity.image'
        db.delete_column(u'charity_app_charity', 'image')


    models = {
        u'charity_app.charity': {
            'Meta': {'object_name': 'Charity'},
            'charity_url': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['charity_app.Video']"})
        },
        u'charity_app.video': {
            'Meta': {'object_name': 'Video'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'video_url': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['charity_app']