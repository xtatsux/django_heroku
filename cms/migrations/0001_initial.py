# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='書籍名', max_length=255)),
                ('publisher', models.CharField(verbose_name='出版社', max_length=255, blank=True)),
                ('page', models.IntegerField(verbose_name='ページ数', blank=True, default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(verbose_name='コメント', blank=True)),
                ('book', models.ForeignKey(verbose_name='書籍', related_name='impressions', to='cms.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
