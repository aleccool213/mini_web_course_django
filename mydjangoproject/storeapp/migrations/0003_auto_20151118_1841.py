# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='name',
            field=models.CharField(max_length=50, default='default name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='purchases',
            field=models.ManyToManyField(to='storeapp.Purchase'),
        ),
    ]
