# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('dimager', '0002_auto_20150303_2109'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProfileQuery',
        ),
        migrations.AddField(
            model_name='imagerprofile',
            name='blocking',
            field=models.ManyToManyField(related_name='_blocking', to='dimager.ImagerProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Entered in the format: '+999999999'. Up to 15 digits allowed.")]),
            preserve_default=True,
        ),
    ]
