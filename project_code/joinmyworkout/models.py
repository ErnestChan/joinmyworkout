from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class User(models.Model):
	GENDER_CHOICES = (('M','Male'), ('F','Female'))

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	age = models.PositiveSmallIntegerField()
	registered_date = models.DateTimeField('date published') #date user registered
	email = models.EmailField()
	karma_points = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.first_name +" "+ self.last_name

@python_2_unicode_compatible  # only if you need to support Python 2
class Event_Type(models.Model):
	"""lookup table for event types and its super class"""
	event_type = models.CharField(max_length=100) #e.g. running, sprints

@python_2_unicode_compatible  # only if you need to support Python 2
class Event_Class(models.Model):
	event_class = models.CharField(max_length=100) #e.g partner sports, team sports

@python_2_unicode_compatible  # only if you need to support Python 2
class Event_Type_To_Class(models.Model):
	event_type = models.ForeignKey(Event_Type, on_delete=models.CASCADE)
	event_class = models.ForeignKey(Event_Class, on_delete=models.CASCADE)

@python_2_unicode_compatible  # only if you need to support Python 2
class Event_Class_To_Experience_Level(models.Model):
	event_class = models.ForeignKey(Event_Class, on_delete=models.CASCADE)
	experience_level = models.CharField(max_length=100)

@python_2_unicode_compatible  # only if you need to support Python 2
class Workout_Event(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	event_name = models.CharField(max_length=100)
	event_type = models.ForeignKey(Event_Type, on_delete=models.CASCADE)
	location = models.CharField(max_length=256)
	time_start = models.TimeField()
	time_end = models.TimeField()
	workout_description = models.TextField(max_length=1500)
	experience
	number_of_spots = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.user+", event: "+event_name+" type: "+event_type

@python_2_unicode_compatible  # only if you need to support Python 2
class Event_History(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	event = models.ForeignKey(Workout_Event, on_delete=models.CASCADE)

