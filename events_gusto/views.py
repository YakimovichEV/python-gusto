from django.shortcuts import render
from main_gusto.models import Event
# Create your views here.


def event_info(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, 'event.html', context={
        'event': event,
    })
