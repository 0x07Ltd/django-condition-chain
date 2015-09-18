# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('module', models.CharField(help_text=b'Module in which the condition function resides', max_length=128)),
                ('function', models.CharField(help_text=b'The function which returns True or False to determine the result of this condition', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ConditionChain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('chain', models.CharField(blank=True, help_text=b'If this is not the first or only rule', max_length=3, choices=[('AND', 'and'), ('OR', 'or')])),
                ('negated', models.BooleanField()),
                ('condition', models.ForeignKey(to='django_condition_chain.Condition')),
            ],
        ),
    ]
