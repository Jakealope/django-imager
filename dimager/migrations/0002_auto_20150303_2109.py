# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dimager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileQuery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='imagerprofile',
            name='birthday_privacy',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imagerprofile',
            name='email_privacy',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imagerprofile',
            name='name_privacy',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imagerprofile',
            name='phone_privacy',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imagerprofile',
            name='picture_privacy',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
