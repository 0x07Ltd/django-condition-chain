# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ConditionChain'
        db.delete_table(u'django_condition_chain_conditionchain')

        # Adding model 'ChainElement'
        db.create_table(u'django_condition_chain_chainelement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chain', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_condition_chain.Chain'])),
            ('joiner', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('negated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('condition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_condition_chain.Condition'])),
        ))
        db.send_create_signal(u'django_condition_chain', ['ChainElement'])

        # Adding model 'Chain'
        db.create_table(u'django_condition_chain_chain', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'django_condition_chain', ['Chain'])


    def backwards(self, orm):
        # Adding model 'ConditionChain'
        db.create_table(u'django_condition_chain_conditionchain', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('chain', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('negated', self.gf('django.db.models.fields.BooleanField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('condition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_condition_chain.Condition'])),
        ))
        db.send_create_signal(u'django_condition_chain', ['ConditionChain'])

        # Deleting model 'ChainElement'
        db.delete_table(u'django_condition_chain_chainelement')

        # Deleting model 'Chain'
        db.delete_table(u'django_condition_chain_chain')


    models = {
        u'django_condition_chain.chain': {
            'Meta': {'object_name': 'Chain'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'django_condition_chain.chainelement': {
            'Meta': {'object_name': 'ChainElement'},
            'chain': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_condition_chain.Chain']"}),
            'condition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_condition_chain.Condition']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joiner': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'negated': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'django_condition_chain.condition': {
            'Meta': {'object_name': 'Condition'},
            'function': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['django_condition_chain']