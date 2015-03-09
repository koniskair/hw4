# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upd_date',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
