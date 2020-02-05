from rest_framework import serializers
from .models import User, Booking, Ticket

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name']



class TicketCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticket
		exclude = ["flight_number", "owner"]

class TicketSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticket
		fields = '__all__'

class TicketBookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticket
		fields = ["flight_number"]
		

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




class BookingListSerializer(serializers.ModelSerializer):
	passenger = UserSerializer()
	ticket = TicketSerializer()
	class Meta:
		model = Booking
		fields = '__all__'


class BookingCreateSerializer(serializers.ModelSerializer):
	ticket = TicketBookingSerializer()

	class Meta:
		model = Booking
		fields = ['ticket']

