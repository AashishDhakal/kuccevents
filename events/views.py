from django.shortcuts import render
from .models import Event

# Create your views here.

def EventListView(request):
    all_events = Event.objects.all()
    return render(request, 'eventlist.html')