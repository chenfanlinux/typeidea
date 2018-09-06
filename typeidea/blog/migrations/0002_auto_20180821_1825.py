# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='status',
            field=models.PositiveIntegerField(verbose_name='状态', default=1, choices=[(1, '正常'), (2, '删除')]),
        ),
    ]
