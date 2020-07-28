from django.contrib import admin
from .models import Event
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'event_date', 'event_time', 'sponsor', 'organizer']
    list_editable = ['event_date', 'event_time']
    search_fields = ['event_name', ]
    list_filter = ['sponsor', 'organizer']


admin.site.register(Event, EventAdmin)