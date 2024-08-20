# todo-note-project

This project is a full-stack application for managing tasks and notes, built with Django on the backend and Vue.js on the frontend.

## Installation
1 Clone the repository
```bash
git clone https://github.com/yourusername/todo-note-project.git
cd todo-note-project
```
2.Backend Setup (Django):
- Create and activate a virtual environment
- Apply migrations and create a superuser:
```bash
python manage.py migrate
python manage.py createsuperuser
```
- Start the Django development server:
```bash
python manage.py runserver
```
3. Frontend Setup (Vue.js):
- Navigate to the frontend directory:
```bash
cd frontend
```
- Install the required npm packages:
```bash
npm install
```
- Start the Vue.js development server:
```bash
npm run serve
```
4. Access the application:
- Backend: `http://localhost:8000/admin` (for Django Admin)
- Frontend: `http://localhost:8080` (for Vue.js frontend)
