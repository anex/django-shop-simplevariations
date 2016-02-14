# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_simplevariations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optiongroup',
            name='products',
            field=models.ManyToManyField(related_name='option_groups', to='shop.Product', blank=True),
        ),
    ]
