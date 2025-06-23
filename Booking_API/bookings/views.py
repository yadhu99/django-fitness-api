from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction
from .models import Fitness_class,Book
from .serializers import Fitness_class_serializer, Book_serializer,BookingDetailSerializer

# Create your views here.
@api_view(['GET'])
def get_classes(request):

    try:
        classes =Fitness_class.objects.filter(available_slots__gt=0)
        serializer=Fitness_class_serializer(classes,many=True)

        return Response({
            'success':True,
            'data':serializer.data,
            'count':len(serializer.data)

        },status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success':False,
            'error':str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def book_class(request):
    try:
        serializer=Book_serializer(data=request.data)
        if serializer.is_valid():
            with transaction.atomic():
                 booking=serializer.save()

                 fitness_class = booking.fitness_class
                 fitness_class.available_slots -= 1
                 fitness_class.save()


                 response_serializer = BookingDetailSerializer(booking)
                 return Response({
                    'success': True,
                    'message': 'Booking confirmed successfully!',
                    'data': response_serializer.data
                }, status=status.HTTP_201_CREATED)
        
        return Response({
            'success': False,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({
            'success': False,
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_bookings(request):
   
    try:
        email = request.query_params.get('email')
        
        if not email:
            return Response({
                'success': False,
                'error': 'Email parameter is required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        bookings = Book.objects.filter(client_email=email)
        serializer = BookingDetailSerializer(bookings, many=True)
        
        return Response({
            'success': True,
            'data': serializer.data,
            'count': len(serializer.data)
        }, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({
            'success': False,
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)       