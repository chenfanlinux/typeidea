# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180821_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.PositiveIntegerField(verbose_name='状态', default=1, choices=[(1, '上线'), (3, '删除')]),
        ),
    ]
