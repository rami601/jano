from django.db import models

# Create your models here.

class Event(models.Model):
    ev_name = models.CharField("event name ",max_length=120)
    ev_date =models.DateField("event date ")
    ev_disc =models.TextField(blank=True)
    ev_manager =models.CharField(max_length=60)
    