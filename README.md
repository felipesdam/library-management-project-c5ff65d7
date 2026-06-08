# library_management_project_c5ff65d7

Library test project

## Prerequisites

- Python 3.8+
- Virtualenv

## Environment Setup

1. **Create and activate a virtual environment:**

    - On Linux/macOS:
      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      ```
    - On Windows:
      ```bash
      py -m venv .venv
      .\.venv\Scripts\activate
      ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Environment Variables Configuration

Create a .env file in the root directory to configure environment variables, such as database settings and secret keys. Example:

```plaintext
DEBUG=True
DJANGO_SECRET_KEY=your-secret-key
```

## Running the Application

Apply database migrations:

```bash
python manage.py makemigrations author
python manage.py makemigrations book
python manage.py makemigrations genre
python manage.py migrate
```

Start the development server:
```bash
python manage.py runserver
```

Access the application in your browser:
```
http://127.0.0.1:8000/
```

## Useful Commands
Create a superuser for accessing Django Admin:
```bash
python manage.py createsuperuser
```
Run tests:
```bash
pytest
```
Verify installed library versions:
```bash
pip list
```
Update requirements.txt with current library versions:
```bash
pip-chill -v > requirements.txt
```
# License
This project is licensed under the MIT License.

---
