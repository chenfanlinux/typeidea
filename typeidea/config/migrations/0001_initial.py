# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='标题', max_length=50)),
                ('href', models.URLField(verbose_name='链接')),
                ('status', models.PositiveIntegerField(verbose_name='状态', default=1, choices=[(1, '正常'), (2, '删除')])),
                ('weight', models.PositiveIntegerField(verbose_name='权重', default=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], help_text='权重越高展示顺序越靠前')),
                ('created_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('owner', models.ForeignKey(verbose_name='作者', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '友链',
                'verbose_name_plural': '友链',
            },
        ),
        migrations.CreateModel(
            name='SideBar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='标题', max_length=50)),
                ('display_type', models.PositiveIntegerField(verbose_name='展示类型', default=1, choices=[(1, 'HTML'), (2, '最新文章'), (3, '最热文章'), (4, '最近评论')])),
                ('content', models.CharField(verbose_name='内容', max_length=50, blank=True, help_text='如果设置的部署html, 可为空')),
                ('created_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('owner', models.ForeignKey(verbose_name='作者', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '侧边栏',
                'verbose_name_plural': '侧边栏',
            },
        ),
    ]
