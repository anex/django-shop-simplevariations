# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import shop.util.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItemOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cartitem', models.ForeignKey(to='shop.CartItem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CartItemTextOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=255)),
                ('cartitem', models.ForeignKey(related_name='text_option', to='shop.CartItem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('price', shop.util.fields.CurrencyField(default=Decimal('0.0'), max_digits=30, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OptionGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('products', models.ManyToManyField(related_name='option_groups', null=True, to='shop.Product', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'A name for this option - this will be displayed to the user', max_length=255)),
                ('description', models.CharField(help_text=b'A longer description for this option', max_length=255, null=True, blank=True)),
                ('price', shop.util.fields.CurrencyField(default=Decimal('0.0'), help_text=b'The price for this custom text', max_digits=30, decimal_places=2)),
                ('products', models.ManyToManyField(related_name='text_options', to='shop.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='option',
            name='group',
            field=models.ForeignKey(to='shop_simplevariations.OptionGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartitemtextoption',
            name='text_option',
            field=models.ForeignKey(to='shop_simplevariations.TextOption'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartitemoption',
            name='option',
            field=models.ForeignKey(to='shop_simplevariations.Option'),
            preserve_default=True,
        ),
    ]
