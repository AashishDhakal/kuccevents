from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class EventAdmin(SummernoteModelAdmin):
    list_display = ['event_name', 'event_date', 'event_time', 'sponsor', 'organizer']
    list_editable = ['event_date', 'event_time']
    search_fields = ['event_name', ]
    list_filter = ['sponsor', 'organizer']
    summernote_fields = ['event_description',]

admin.site.register(Event, EventAdmin)