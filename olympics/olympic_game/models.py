from django.db import models
from django.utils import timezone

class Athlete(models.Model):
    name = models.CharField(max_length=100)
    # participating_events = models.ManyToManyField(Event, through='AthleteEvent')
    def __str__(self):
        return self.name

class Event(models.Model):
    indoor = True
    mens_event = True

class AthleteEvent(models.Model):
    event = models.ForeignKey(Event,related_name="event", on_delete=models.CASCADE)
    event_date_time = models.DateTimeField(null=True)
    event_location = models.CharField(max_length=150)
    gold_medal_winner = models.ForeignKey(Athlete, related_name="gold_medal_winner")
    silver_medal_winner = models.ForeignKey(Athlete, related_name="silver_medal_winner")
    bronze_medal_winner = models.ForeignKey(Athlete, related_name="bronze_medal_winner")

    def schedule_event_date(self):
        self.event_date_time = timezone.now()
        self.save()
