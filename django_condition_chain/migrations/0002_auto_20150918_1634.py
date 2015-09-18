# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_condition_chain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ChainElement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('joiner', models.CharField(blank=True, max_length=3, choices=[('AND', 'and'), ('OR', 'or')])),
                ('negated', models.BooleanField(default=False)),
                ('chain', models.ForeignKey(to='django_condition_chain.Chain')),
                ('condition', models.ForeignKey(to='django_condition_chain.Condition')),
            ],
        ),
        migrations.RemoveField(
            model_name='conditionchain',
            name='condition',
        ),
        migrations.DeleteModel(
            name='ConditionChain',
        ),
    ]
