import uuid

import os
from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from website.apps.salesbro.models import Ticket, TicketOption
from sorl.thumbnail import ImageField


class Convention(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return '{name}'.format(name=self.name)


def rename_thumb(instance, filename):
        extension = filename.split('.')[-1]
        filename = '%s.%s' % (uuid.uuid4(), extension)
        return os.path.join('eventbro/thumbs', filename)


class Event(models.Model):
    BYOC_LAN = u'LAN'
    MINIATURES = u'MIN'
    TABLETOP = u'TAB'
    RPG = u'RPG'
    EVENT_TYPE_CHOICES = (
        (BYOC_LAN, u'BYOC LAN'),
        (MINIATURES, u'Miniatures'),
        (TABLETOP, u'Tabletop'),
        (RPG, u'RPG'),
    )

    convention = models.ForeignKey(Convention, related_name='event_convention_id')
    name = models.CharField(verbose_name='Event Name', max_length=100)
    description = models.TextField(blank=True, null=True)
    start = models.DateTimeField(verbose_name='Start Time')
    end = models.DateTimeField(verbose_name='End Time')
    size = models.PositiveSmallIntegerField(verbose_name='Max Size', blank=True, null=True)
    published = models.BooleanField(default=False)
    valid_options = models.ManyToManyField(TicketOption, related_name='event_valid_tickets',
                                           verbose_name='Valid participants')
    group_event = models.BooleanField(default=False, verbose_name='Is group event')
    require_game_id = models.BooleanField(default=False, verbose_name='Require special ID')
    game_id_name = models.CharField(max_length=100, blank=True, null=True,
                                    verbose_name='Unique identifier')
    event_type = models.CharField(max_length=3, choices=EVENT_TYPE_CHOICES, blank=True, null=True)
    image = ImageField(upload_to=rename_thumb, blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Event, self).save()

        # Thumbnail all images
        if self.image:
            # presets
            max_width = 200
            max_height = 100
            max_size = (max_width, max_height)

            image = Image.open(self.image.path)
            width, height = image.size
            if height > max_height:
                image.thumbnail(size=max_size, resample=Image.ANTIALIAS)
                image.save(self.image.path)


class Registration(models.Model):
    user = models.ForeignKey(User, related_name='registration_user')
    event = models.ForeignKey(Event, related_name='registration_event')
    date_added = models.DateTimeField(auto_now_add=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    group_captain = models.BooleanField(default=False)
    game_id = models.CharField(max_length=255, blank=True, null=True)

