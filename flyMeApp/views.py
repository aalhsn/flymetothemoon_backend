# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import TicketSerializer, UserCreateSerializer, BookingListSerializer, BookingCreateSerializer, TicketCreateSerializer
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import uuid
from rest_framework.filters import SearchFilter
from .models import Booking, Ticket

# Create your views here.
class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

class BookingCreateAPIView(CreateAPIView):
	serializer_class = BookingCreateSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(passenger=self.request.user, booking_ref=str(uuid.uuid4())[:4].upper())
	

class TicketCreateAPIView(CreateAPIView):
	serializer_class = TicketCreateSerializer
	permission_classes = [IsAuthenticated, IsAdminUser]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user,flight_number="MN 0"+str(uuid.uuid4().int)[:3])

class BookingListAPIView(ListAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingListSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Booking.objects.filter(passenger=self.request.user)

class FlightListAPIView(ListAPIView):
	queryset = Ticket.objects.all()
	serializer_class = TicketSerializer

