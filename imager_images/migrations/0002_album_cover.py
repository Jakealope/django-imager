# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ForeignKey(related_name='+', blank=True, to='imager_images.Photo', null=True),
            preserve_default=True,
        ),
    ]
