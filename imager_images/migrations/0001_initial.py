# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, blank=True)),
                ('description', models.TextField(blank=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('date_modified', models.DateField(auto_now=True, null=True)),
                ('date_publishd', models.DateField(null=True, blank=True)),
                ('PUBLISHED', models.CharField(default=b'private', max_length=3, choices=[(b'private', b'private'), (b'shared', b'shared'), (b'public', b'public')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'photos')),
                ('title', models.CharField(max_length=100, blank=True)),
                ('description', models.TextField(blank=True)),
                ('date_uploaded', models.DateField(auto_now_add=True, null=True)),
                ('date_modified', models.DateField(auto_now=True, null=True)),
                ('date_publishd', models.DateField(null=True, blank=True)),
                ('PUBLISHED', models.CharField(default=b'private', max_length=3, choices=[(b'private', b'private'), (b'shared', b'shared'), (b'public', b'public')])),
                ('user', models.ForeignKey(related_name='photo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='album',
            name='pictures',
            field=models.ManyToManyField(related_name='album', to='imager_images.Photo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(related_name='album', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
