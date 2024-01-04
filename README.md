# Taskify - Simplifying Task Management 📋

Taskify is a platform designed to streamline the process of managing tasks. It empowers users to effortlessly create, edit, and delete tasks, offering a user-friendly task management experience.

## Features
- **Add Task:** Easily add tasks for efficient management.
- **Edit Task:** Modify task details as needed.
- **Delete Task:** Remove tasks that are completed or no longer relevant.

## Frontend API Consumption

We consume the REST API in the frontend using Python's `requests` library. For more information about the `requests` library, refer to the [official documentation](https://requests.readthedocs.io/en/latest/).

### Technology Stack
- **Frontend:**
  - HTML 🌐
  - CSS 🎨
  - JavaScript 🖥️
  - Bootstrap 🅱️

- **Backend:**
  - Python 🐍
  - Django 🌐

- **Database:** 
  - MySQL 🗃️

- **API:**
  - Django REST framework (for RESTful API) 🔌

### API Endpoints
- **Base URL for API Information:** `http://127.0.0.1:8000/api/` (List of all endpoints)

- `http://127.0.0.1:8000/api/list/` (GET method)
  - Lists all tasks available in the database irrespective of the user.

- `http://127.0.0.1:8000/api/list/id/` (GET method)
  - Shows the details of each task based on the ID irrespective of the user.

- `http://127.0.0.1:8000/api/signup/` (POST method)
  - Creates an account in the API.
  - JSON Payload:
    ```json
    {
        "username": "test1",
        "password1": "test123@Pass",
        "password2": "test123@Pass"
    }
    ```

- `http://127.0.0.1:8000/api/login/` (POST method)
  - Logs in and retrieves the token for authentication (requires passing username, password).
  - JSON Payload:
    ```json
    {
        "username": "test1",
        "password": "test123@Pass"
    }
    ```

- `http://127.0.0.1:8000/api/create/` (POST method)
  - Endpoint for creating a new task.
  - JSON Payload:
    ```json
    {
        "title": "sample title",
        "desc": "sample description",
        "complete": false
    }
    ```

- `http://127.0.0.1:8000/api/mytasks/` (GET method)
  - Only authenticated users can access their task list (token needed).

- `http://127.0.0.1:8000/api/mytasks/id/` (GET method)
  - Detailed view of a specific task accessible only to authenticated users.

- `http://127.0.0.1:8000/api/update/id/` (PATCH method)
  - Updates a task based on ID.
  - JSON Payload:
    ```json
    {
        "title": "updated title",
        "desc": "updated description",
        "complete": true
    }
    ```

- `http://127.0.0.1:8000/api/delete/id/` (DELETE method)
  - Authenticated users can delete the task.


### Additional Security Features
- **Object Level Permissions:**
  - Implemented to restrict viewing, editing, and deleting data to only the object's owner.
  - Code present in `custom_permissions.py` file in the API app:
    ```python
    from rest_framework import permissions

    class IsObjectOwnerOrReject(permissions.BasePermission):
        def has_object_permission(self, request, view, obj):
            return obj.user == request.user
    ```

- **API Rate Limiting:**
  - Implemented for `http://127.0.0.1:8000/api/list/` (GET request) and `http://127.0.0.1:8000/api/list/id/`.
  - Custom rate limiting available in `throttles.py` file:
    ```python
    from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
    from django.core.cache import caches

    class BurstRateThrottle(AnonRateThrottle):
        scope = "burst"

    class SimpleRateThrottle(AnonRateThrottle):
        scope = "simple"
    ```
  - Apply custom rate limiting for different endpoints as needed.


### Authentication
- Token-based authentication for secure user interactions.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    $ git clone https://github.com/Prathish14/taskify-django.git
    $ cd Taskify
    ```

2. **Install dependencies** from `requirements.txt`:
    ```bash
    $ pip install -r requirements.txt
    ```

3. **Configure Database:**
   - Set up your MySQL database credentials in `settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'Your_Database_Name',
            'USER': 'Your_Database_User',
            'PASSWORD': 'Your_Database_Password',
            'HOST': 'Your_Database_Host',
            'PORT': 'Your_Database_Port',
        }
    }
    ```

4. **Configure REST Framework Settings:**
   - Add REST Framework settings to `settings.py` after database settings:
    ```python
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            "rest_framework.authentication.TokenAuthentication",
        ],

        'DEFAULT_THROTTLE_CLASSES': [
            'rest_framework.throttling.ScopedRateThrottle',
        ],

        'DEFAULT_THROTTLE_RATES': {
            'burst': '15/hour',
            'simple': '10/day'
        }
    }
    ```

5. **Start the Django server:**
    ```bash
    $ python manage.py migrate
    $ python manage.py runserver
    ```

6. **Access the application** in your browser at `http://localhost:8000/`.

## Usage

Once the server is running, you can interact with the Taskify application by accessing the provided API endpoints.

## Contributing

Contributions are welcome! To contribute to Taskify:
- Fork the repository
- Create a new branch (`git checkout -b feature`)
- Make your changes
- Commit your changes (`git commit -am 'Add feature'`)
- Push to the branch (`git push origin feature`)
- Create a new Pull Request
