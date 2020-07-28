from django.urls import path
from .views import EventListView

urlpatterns = [
    path('', EventListView, name='eventlist'),
]