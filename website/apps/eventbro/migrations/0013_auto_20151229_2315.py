# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields
import website.apps.eventbro.models


class Migration(migrations.Migration):

    dependencies = [
        ('eventbro', '0012_auto_20151216_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[('LAN', 'BYOC LAN'), ('MIN', 'Miniatures'), ('RPG', 'RPG'), ('TAB', 'Tabletop')]),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=website.apps.eventbro.models.rename_image, blank=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='event',
            field=models.ForeignKey(related_name='registrants', to='eventbro.Event'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='game_id',
            field=models.CharField(help_text=b'eg Battle.net ID, Summoner ID, etc', max_length=255, null=True, verbose_name=b'Game ID', blank=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='group_name',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Group Name', blank=True),
        ),
    ]