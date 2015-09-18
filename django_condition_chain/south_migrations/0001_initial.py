# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Condition'
        db.create_table(u'django_condition_chain_condition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('module', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('function', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'django_condition_chain', ['Condition'])

        # Adding model 'ConditionChain'
        db.create_table(u'django_condition_chain_conditionchain', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('chain', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('negated', self.gf('django.db.models.fields.BooleanField')()),
            ('condition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_condition_chain.Condition'])),
        ))
        db.send_create_signal(u'django_condition_chain', ['ConditionChain'])


    def backwards(self, orm):
        # Deleting model 'Condition'
        db.delete_table(u'django_condition_chain_condition')

        # Deleting model 'ConditionChain'
        db.delete_table(u'django_condition_chain_conditionchain')


    models = {
        u'django_condition_chain.condition': {
            'Meta': {'object_name': 'Condition'},
            'function': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'django_condition_chain.conditionchain': {
            'Meta': {'object_name': 'ConditionChain'},
            'chain': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'condition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_condition_chain.Condition']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'negated': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['django_condition_chain']