# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0003_auto_20151118_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]
