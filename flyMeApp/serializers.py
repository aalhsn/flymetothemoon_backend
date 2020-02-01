from rest_framework import serializers
from .models import User, Booking, Ticket

class TicketCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticket
		fields = '__all__'
		exclude = ["flight_number", "owner"]

class TicketSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticket
		fields = '__all__'
		

class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username','password','first_name','last_name']

	def create(self, validated_data):
		first_name = validated_data['first_name']
		last_name = validated_data['last_name']
		username = validated_data['username']
		new_user = User(first_name=first_name, last_name=last_name, username=username)
		new_user.email = (validated_data['username'])
		new_user.set_password(validated_data['password'])
		new_user.save()
		print("User saved")
		return validated_data

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticket
		fields = ['username', 'first_name', 'last_name']


class BookingListSerializer(serializers.ModelSerializer):
	Tickets = TicketSerializer(many=True)

	class Meta:
		model = Booking
		fields = ['Tickets', 'passenger']


class BookingCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ["ticket"]
