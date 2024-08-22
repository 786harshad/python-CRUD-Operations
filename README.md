# Django User Management System

This Django project is an User Management System where you can manage user records via the Django admin interface.

## Setup and Installation

### Prerequisites

- Python 3.x
- Django 4.2
- MySQL 8.0.18 (or compatible)

### Cloning the Repository

git clone <repository-url>
cd <project-directory>

####  Install Dependencies
Ensure you have a virtual environment set up and activate it. Install the required Python packages:

#### Database Setup
The project uses MySQL for the database. Ensure that MySQL is installed and running.

The database configuration is specified in settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangodb',  # Replace with your database name
        'USER': 'root',      # Replace with your database user
        'PASSWORD': '',      # Replace with your database password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

#### Migrations
Run the following commands to create the necessary database tables:

python manage.py makemigrations
python manage.py migrate

### Accessing the Admin Interface
Once the server is running, you can access the Django admin interface at:

URL: http://localhost:8000/admin/
Username: admin@test.com
Password: admin123#

