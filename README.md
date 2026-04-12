# MediData

A Django-based medical data management application with user authentication and profile management.

# LiveDemo
https://medical-bill-extract-2ashatbzcxn9fkhejaxboe.streamlit.app/

## Features

- **User Authentication**: Secure registration and login system
- **User Profiles**: Manage user information including date of birth
- **Dashboard**: Personalized dashboard for authenticated users
- **Responsive Design**: Clean and user-friendly interface

## Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.8+**
- **PostgreSQL** (or another database supported by Django)
- **pip** (Python package installer)
- **Git** (optional, for cloning the repository)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd MediData
```

### 2. Create a Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory of the project with the following variables:

```
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgres://username:password@localhost:5432/medidata
ALLOWED_HOSTS=localhost,127.0.0.1
```

**Note:** Replace `username`, `password`, and `medidata` with your PostgreSQL credentials and database name.

### 5. Create the Database (PostgreSQL)

```bash
createdb medidata
```

Alternatively, use a PostgreSQL client GUI like pgAdmin to create a new database.

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

## Running the Project

### Start the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

### Access the Application

- **Home Page**: `http://127.0.0.1:8000/`
- **Registration**: `http://127.0.0.1:8000/register/`
- **Login**: `http://127.0.0.1:8000/login/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/` (use superuser credentials)

## Project Structure

```
MediData/
├── MediData/                 # Main Django app
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   │   └── MediData/
│   │       ├── home.html
│   │       ├── login.html
│   │       └── register.html
│   ├── models.py            # Database models
│   ├── views.py             # View logic
│   ├── forms.py             # Form definitions
│   ├── urls.py              # App URL routing
│   └── admin.py             # Admin configuration
├── myproject/               # Project settings
│   ├── settings.py          # Configuration settings
│   ├── urls.py              # Main URL routing
│   └── wsgi.py              # WSGI configuration
├── attachments/             # Media files directory
├── manage.py                # Django management script
└── requirements.txt         # Python dependencies
```

## Database Models

### Profile
- **User**: OneToOne relationship with Django User model
- **DOB**: Date of birth field (optional)

## Dependencies

- **Django 6.0.4**: Web framework
- **psycopg2-binary 2.9.11**: PostgreSQL adapter
- **python-dotenv 1.2.2**: Environment variable management
- **dj-database-url 3.1.2**: Database URL parsing
- **sqlparse 0.5.5**: SQL parsing library
- **tzdata 2026.1**: Timezone database
- **asgiref 3.11.1**: ASGI utilities

## Common Commands

### Create a New App

```bash
python manage.py startapp app_name
```

### Make Migrations (after model changes)

```bash
python manage.py makemigrations
```

### Apply Migrations

```bash
python manage.py migrate
```

### Access Django Shell

```bash
python manage.py shell
```

### Collect Static Files (before production)

```bash
python manage.py collectstatic
```

### Run Tests

```bash
python manage.py test
```

## Troubleshooting

### Database Connection Error

- Ensure PostgreSQL is running on your machine
- Verify the `DATABASE_URL` in your `.env` file is correct
- Check that the database exists in PostgreSQL

### Migration Errors

```bash
python manage.py migrate --run-syncdb
```

### Port Already in Use

If port 8000 is already in use:

```bash
python manage.py runserver 8001
```

### Module Not Found

Ensure your virtual environment is activated and dependencies are installed:

```bash
pip install -r requirements.txt
```

## Deployment

For production deployment, consider using:

- **Gunicorn**: WSGI HTTP Server
- **Nginx**: Reverse proxy server
- **Docker**: Containerization
- **AWS/Heroku/DigitalOcean**: Hosting platforms

Update `ALLOWED_HOSTS` and `DEBUG=False` in settings for production.

## Contributing

1. Create a feature branch: `git checkout -b feature-name`
2. Commit changes: `git commit -am 'Add feature'`
3. Push to branch: `git push origin feature-name`
4. Submit a pull request

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Support

For issues or questions, please contact the development team or open an issue on the project repository.

---

**Last Updated**: April 2026
