from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class Fitness_class(models.Model):
    TYPES=[
        ('zumba','Zumba'),
        ('yoga','Yoga'),
        ('hiit','HIIT'),
    ]

    name=models.CharField(max_length=100)
    fitness_type=models.CharField(max_length=20, choices=TYPES)
    date_time=models.DateTimeField()
    instructor=models.CharField(max_length=50)
    total_slots=models.PositiveIntegerField(validators=[MinValueValidator(1)])
    available_slots=models.PositiveIntegerField()
    craeted_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['date_time']

    def __str__(self):
        return f"{self.name} - {self.date_time.strftime('%Y-%m-%d %H:%M')}"
    
    def save(self, *args, **kwargs):
        
        if not self.pk:
            self.available_slots = self.total_slots
        super().save(*args, **kwargs)


class Book(models.Model):
    fitness_class=models.ForeignKey(Fitness_class, on_delete=models.CASCADE)
    client_name=models.CharField(max_length=50)
    client_id=models.CharField(max_length=10)
    client_email=models.EmailField()
    booking_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        
        unique_together = ['fitness_class', 'client_email']
        ordering = ['-booking_date']
    
    def __str__(self):
        return f"{self.client_name} - {self.fitness_class.name}"
    
    