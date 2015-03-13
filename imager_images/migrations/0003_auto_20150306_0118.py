# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0002_album_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='PUBLISHED',
            field=models.CharField(default=b'private', max_length=10, choices=[(b'private', b'private'), (b'shared', b'shared'), (b'public', b'public')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='PUBLISHED',
            field=models.CharField(default=b'private', max_length=10, choices=[(b'private', b'private'), (b'shared', b'shared'), (b'public', b'public')]),
            preserve_default=True,
        ),
    ]
