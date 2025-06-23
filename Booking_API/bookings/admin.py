from django.contrib import admin

# Register your models here.

from .models import Fitness_class, Book

@admin.register(Fitness_class)
class FitnessClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'fitness_type', 'date_time', 'instructor', 'available_slots', 'total_slots']
    list_filter = ['fitness_type', 'date_time']
    search_fields = ['name', 'instructor']
    ordering = ['date_time']

@admin.register(Book)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_email', 'fitness_class', 'booking_date']
    list_filter = ['booking_date', 'fitness_class__fitness_type']
    search_fields = ['client_name', 'client_email']
    readonly_fields = ['booking_date']