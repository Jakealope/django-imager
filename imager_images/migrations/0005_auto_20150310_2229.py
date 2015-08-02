# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0004_auto_20150310_1948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='date_publishd',
            new_name='date_published',
        ),
    ]
