# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_is_markdown'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='html',
            field=models.TextField(verbose_name='渲染后的内容', default='', help_text='正文必须是markdown格式'),
        ),
    ]
