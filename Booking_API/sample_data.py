# Create a file: add_sample_data.py in your project root
import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Booking_API.settings')
django.setup()

from bookings.models import Fitness_class

# Create sample fitness classes
classes_data = [
    {
        'name': 'Morning Zumba',
        'fitness_type': 'zumba',
        'date_time': datetime.now() + timedelta(days=1, hours=9),
        'instructor': 'Maria Rodriguez',
        'total_slots': 20,
    },
    {
        'name': 'Sunrise Yoga',
        'fitness_type': 'yoga',
        'date_time': datetime.now() + timedelta(days=1, hours=7),
        'instructor': 'Sarah Johnson',
        'total_slots': 15,
    },
    {
        'name': 'Evening HIIT',
        'fitness_type': 'hiit',
        'date_time': datetime.now() + timedelta(days=1, hours=18),
        'instructor': 'Mike Thompson',
        'total_slots': 12,
    },
    {
        'name': 'Weekend Zumba',
        'fitness_type': 'zumba',
        'date_time': datetime.now() + timedelta(days=2, hours=10),
        'instructor': 'Carlos Martinez',
        'total_slots': 25,
    },
]

for class_data in classes_data:
    Fitness_class.objects.create(**class_data)
    print(f"Created: {class_data['name']}")

print("Sample data created successfully!")