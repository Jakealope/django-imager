# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('dimager', '0003_auto_20150305_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagerprofile',
            name='following',
            field=models.ManyToManyField(related_name='_following', to='dimager.ImagerProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='user',
            field=models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
