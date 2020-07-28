from django.shortcuts import render
from .models import Event

# Create your views here.

def EventListView(request):
    all_events = Event.objects.all().order_by('event_date')
    return render(request, 'eventlist.html', {'allevents': all_events, })

def EventDetailView(request, pk):
    event = Event.objects.get(id=pk)
    return render(request, 'eventdetails.html', {'event': event, })