# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-20 04:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='コメント')),
                ('createdate', models.DateTimeField(auto_now_add=True)),
                ('good', models.IntegerField(default=0)),
                ('authid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL, verbose_name='投稿者')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=255, verbose_name='テーマ')),
                ('text', models.TextField(blank=True, verbose_name='説明')),
                ('is_enforce', models.BooleanField(default=False)),
                ('createdate', models.DateTimeField(auto_now_add=True)),
                ('updatedate', models.DateTimeField(auto_now=True)),
                ('authid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theme', to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='themeid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='chat.Theme', verbose_name='投稿先'),
        ),
    ]
