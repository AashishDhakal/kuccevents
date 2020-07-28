from django.urls import path
from .views import EventListView, EventDetailView

urlpatterns = [
    path('', EventListView, name='eventlist'),
    path('detail/<pk>/', EventDetailView, name='eventdetail'),
]