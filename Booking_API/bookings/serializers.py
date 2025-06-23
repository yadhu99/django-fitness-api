from datetime import timezone
from rest_framework import serializers
from .models import Fitness_class,Book

class Fitness_class_serializer(serializers.ModelSerializer):
    class Meta:
        model=Fitness_class
        fields=['id','name','fitness_type','date_time','instructor','available_slots']

class Book_serializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['fitness_class','client_name','client_id','client_email']

        def validate(self,data):
             
             fitness_class=data['fitness_class']

             
             if fitness_class.available_slots<=0:
                 raise serializers.ValidationError("No available slots for this class")
             
             if fitness_class.date_time <= timezone.now():
                 raise serializers.ValidationError("Cannoy Book Past Classes")
             
             if Book.object.filter(
                 fitness_class=fitness_class,
                 client_email=data['client_email']

             ).exists():
                 raise serializers.ValidationError("You have already booked this class")
             
             return data


class BookingDetailSerializer(serializers.ModelSerializer):
    fitness_class = Fitness_class_serializer(read_only=True)
    
    class Meta:
        model = Book
        fields = ['id', 'fitness_class', 'client_name', 'client_id', 'client_email', 'booking_date']
    
