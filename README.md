# django-fitness-api


 Django Fitness Center API

A RESTful API to manage fitness class schedules and client bookings using Django and Django REST Framework.

---

Features

- Create and manage fitness classes ('Zumba', 'Yoga', 'HIIT')
- Book classes with availability tracking
- Prevent double bookings
- View bookings by client email
- Admin interface for managing classes and bookings
- Sample data population script



 Tech Stack

- Python 3.8+
- Django
- Django REST Framework
- SQLite (default, easy to change)




Prerequisites

- Python 3.8+
- pip
- Code editor (VS Code recommended)



 Setup Instructions
 1. Clone the Repository


git clone https://github.com/yadhu99/django-fitness-api



2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv any_name

# Activate
# Windows
env_name\Scripts\activate

# macOS/Linux
source env_name/bin/activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

```

6. Populate Sample Data

```bash
python add_sample_data.py
```

7. Run the Server

```bash
python manage.py runserver
```

Server will be available at: `http://127.0.0.1:8000/`

---
 📡 API Endpoints

 GET /api/classes/

Returns a list of available fitness classes.

```bash
curl http://localhost:8000/api/classes/
```

---

POST /api/book/

Book a class by providing fitness_class ID and client details.

```bash
curl -X POST http://localhost:8000/api/book/ \

-H "Content-Type: application/json" \
-d '{
    "fitness_class": 1,
    "client_name": "",
    "client_id": "",
    "client_email": ""
}'
```

---

GET /api/bookings/?email=user@example.com

Returns a list of bookings made by the specified email.

```bash
curl "http://localhost:8000/api/bookings/?email=any_name@email.com"
```

---

 Admin Panel

Visit `http://localhost:8000/admin` and log in using the superuser credentials.

You can:
- Create, update, or delete fitness classes
- View and manage bookings

---
