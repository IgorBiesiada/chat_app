# Real-Time Chat Application — Django, Django REST Framework, WebSockets, Vue.js  

## Project Overview  

This is a real-time chat application built with **Django**, **Django REST Framework**, and **Django Channels** for WebSocket support.  
The app provides user registration, login, friend management, and real-time messaging.  

The frontend will be developed in **Vue.js**, and the entire project is planned to be containerized with **Docker**.  
The application uses **PostgreSQL** as the main database and **Redis** as a WebSocket message broker.  
**Daphne** is used as the ASGI server.  

⚡ **This project is under active development — some features are still in progress or planned for future updates.**  

---

## Technologies Used  

- **Django** — backend, authentication system, user management  
- **Django REST Framework** — API for users, friends, and messages  
- **Django Channels** — WebSocket support for real-time messaging  
- **Daphne** — ASGI server  
- **PostgreSQL** — relational database  
- **Redis** — message broker for WebSocket handling  
- **Vue.js** *(planned)* — frontend framework  
- **Docker** *(planned)* — containerized deployment  

---

## Project Status  

- ✅ User registration and login system  
- ✅ Friend management system *(in progress)*  
- ✅ Real-time chat with WebSocket support *(in progress)*  
- 🚧 Vue.js frontend *(planned)*  
- 🚧 Docker integration *(planned)*  

---

## Installation (Development Mode)  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/YourUsername/your-chat-app.git  
   cd your-chat-app  

2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv  
    source venv/bin/activate  
    pip install -r requirements.txt

3. Apply migrations and run the development server with Daphne:
    ```bash
    python manage.py migrate  
    daphne -b 0.0.0.0 -p 8000 your_project_name.asgi:application

## Plans for Development

- ✅ Build basic user registration and login with Django Auth
- ✅ Implement WebSocket-based real-time chat using Django Channels
- ✅ Integrate PostgreSQL and Redis
- ✅ Develop friend management system
- 🛠️ Build frontend with Vue.js (real-time chat interface, friend system)
- 🛠️ Set up full Docker environment with docker-compose
- 🛠️ Deploy production-ready setup with Daphne, Redis, and secure WebSocket         communication
- 🛠️ Write automated tests for key functionalities
- 🛠️ Improve WebSocket events handling and error management