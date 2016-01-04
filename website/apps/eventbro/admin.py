from django.contrib import admin

from website.apps.eventbro.models import Convention, Event, Registration, Sponsor, EventType

from sorl.thumbnail.admin import AdminImageMixin


class ConventionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                ('name', 'published',),
                ('start', 'end',),
            )
        }),
        ('Details', {
            'fields': ('description',)
        }),
    )

    list_display = ['name', 'start', 'end']

    # list_filter = ("order", "ticket")


class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'overlapping')

class EventAdmin(AdminImageMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
               ('name',),
               ('convention', 'event_type',),
               ('published',),
               ('start', 'end',),
               ('description',),
            ),
        }),
        ('Details', {
            'fields': (
                ('size',),
                ('valid_options',),
                ('group_event',),
                ('require_game_id', 'game_id_name',),
            ),
        }),
        ('Image', {
            'fields': (
                ('image',),
            ),
        }),
        ('Other Details', {
            'fields': (
                ('sponsor',),
                ('organizer',),
                ('prizes',),
                ('rules',),
            ),
        }),
    )
    list_display = ('name', 'event_type', 'convention', 'size', 'start', 'end',)

    list_filter = ('name', 'event_type', 'convention',)


class RegistrationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Required', {
            'fields': (
                ('user', 'event',),
                ('date_added',),
            )
        }),
        ('Optional', {
            'fields': (
                ('group_name', 'group_captain',),
                ('game_id',),
            )
        }),
    )

    readonly_fields = ('date_added',)

    list_display = ('id', 'user', 'event', 'date_added', 'game_id', 'group_name', 'group_captain')

    list_filter = ('user', 'event')


class SponsorAdmin(AdminImageMixin, admin.ModelAdmin):
    fieldsets = (
        ('Required', {
            'fields': (
                ('name',),
                ('description',),
                ('logo',),
                ('level',),
                ('convention',),
            )
        }),
        # ('Optional', {
        #     'fields': (
        #         ('group_name', 'group_captain',),
        #         ('game_id',),
        #     )
        # }),
    )

    list_display = ('id', 'name', 'level', 'convention')

    list_filter = ('level', 'convention')


admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Convention, ConventionAdmin)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Sponsor, SponsorAdmin)
