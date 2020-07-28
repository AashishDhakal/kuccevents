from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_description = models.TextField()
    event_date = models.DateField()
    event_time = models.TimeField()
    sponsor = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100)

    def __str__(self):
        return self.event_name