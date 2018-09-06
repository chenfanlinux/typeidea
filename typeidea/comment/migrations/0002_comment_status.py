# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.PositiveIntegerField(verbose_name='状态', default=1, choices=[(1, '展示'), (2, '下线')]),
        ),
    ]
