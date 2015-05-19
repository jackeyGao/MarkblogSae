# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='is_reply',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u8bc4\u8bba'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='is_valid',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(unique=True, max_length=45, verbose_name='\u65e5\u5fd7URL'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(unique=True, max_length=50, verbose_name='\u65e5\u5fd7\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='blogtemplate',
            name='name',
            field=models.CharField(unique=True, max_length=20, verbose_name='\u6a21\u677f\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(unique=True, max_length=20, verbose_name='\u7c7b\u76ee\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(unique=True, max_length=50, verbose_name='\u6807\u7b7e\u540d\u79f0'),
        ),
    ]
