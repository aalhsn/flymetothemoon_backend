# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User



class Ticket(models.Model):
	flight_number = models.CharField(max_length=30)
	start_date = models.DateField()
	start_time = models.TimeField()
	end_time = models.TimeField()
	end_date = models.DateField()
	description = models.TextField(null=True)
	price=models.DecimalField(max_digits=7, decimal_places=3, validators=[MinValueValidator(0.0)])
	qty = models.IntegerField()
	owner=models.ForeignKey(User, on_delete=models.CASCADE, related_name='ticket_owner')

 
	def __str__(self):
		return self.flight_number


	def __str__(self):
		return self.first_name+" "+self.last_name

class Booking(models.Model):
	ticket=models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='booked_flight')
	passenger=models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
	booking_ref=models.CharField(max_length=30)
	

	def __str__(self):
		return self.ticket.flight_number+" - "+self.passenger.last_name