# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Confirmation'
        db.create_table('librelist_confirmation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('request_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('expected_secret', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pending_message_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('list_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('librelist', ['Confirmation'])

        # Adding model 'UserState'
        db.create_table('librelist_userstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('state_key', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('from_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('librelist', ['UserState'])

        # Adding model 'Domain'
        db.create_table('librelist_domain', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('librelist', ['Domain'])

        # Adding M2M table for field owners on 'Domain'
        db.create_table('librelist_domain_owners', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('domain', models.ForeignKey(orm['librelist.domain'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('librelist_domain_owners', ['domain_id', 'user_id'])

        # Adding model 'MailingList'
        db.create_table('librelist_mailinglist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('archive_url', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('archive_queue', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('similarity_pri', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('similarity_sec', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('domain', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['librelist.Domain'])),
        ))
        db.send_create_signal('librelist', ['MailingList'])

        # Adding M2M table for field owners on 'MailingList'
        db.create_table('librelist_mailinglist_owners', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mailinglist', models.ForeignKey(orm['librelist.mailinglist'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('librelist_mailinglist_owners', ['mailinglist_id', 'user_id'])

        # Adding model 'Subscription'
        db.create_table('librelist_subscription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('subscriber_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('subscriber_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('mailing_list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['librelist.MailingList'])),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('librelist', ['Subscription'])


    def backwards(self, orm):
        # Deleting model 'Confirmation'
        db.delete_table('librelist_confirmation')

        # Deleting model 'UserState'
        db.delete_table('librelist_userstate')

        # Deleting model 'Domain'
        db.delete_table('librelist_domain')

        # Removing M2M table for field owners on 'Domain'
        db.delete_table('librelist_domain_owners')

        # Deleting model 'MailingList'
        db.delete_table('librelist_mailinglist')

        # Removing M2M table for field owners on 'MailingList'
        db.delete_table('librelist_mailinglist_owners')

        # Deleting model 'Subscription'
        db.delete_table('librelist_subscription')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'librelist.confirmation': {
            'Meta': {'object_name': 'Confirmation'},
            'expected_secret': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'from_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pending_message_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'request_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'librelist.domain': {
            'Meta': {'object_name': 'Domain'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'owners': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'})
        },
        'librelist.mailinglist': {
            'Meta': {'object_name': 'MailingList'},
            'archive_queue': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'archive_url': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['librelist.Domain']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'owners': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'similarity_pri': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'similarity_sec': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        },
        'librelist.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailing_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['librelist.MailingList']"}),
            'subscriber_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'subscriber_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'librelist.userstate': {
            'Meta': {'object_name': 'UserState'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'state_key': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['librelist']