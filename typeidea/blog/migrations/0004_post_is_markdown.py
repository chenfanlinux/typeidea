# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180824_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_markdown',
            field=models.BooleanField(verbose_name='使用markdown格式', default=True),
        ),
    ]
