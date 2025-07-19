# taskManager_API
This is a Task Manager API that allows software applications to interact with a task management system, i.e., a system that handles the creation, scheduling, execution, monitoring, and management of tasks or jobs.

# ✅ Task Manager Backend API

A FastAPI-powered backend project that provides secure, scalable task management for registered users. Features include JWT-based authentication, user-specific task CRUD, and Docker-based deployment.

---

## 🚀 Features

- 🔐 User Registration & Login (JWT Auth)
- 📋 Task CRUD (Create, Read, Update, Delete)
- 📅 Due date tracking & status updates
- 🧾 SQLite database (easy to extend to PostgreSQL)
- ⚙️ Dockerized setup
- 📜 Auto-generated API docs (Swagger & ReDoc)

---

## 🛠️ Tech Stack

- **FastAPI** – High-performance Python web framework
- **SQLAlchemy** – ORM for database models
- **SQLite** – Lightweight DB (swap with PostgreSQL for production)
- **JWT** – Secure token-based authentication
- **Docker** – Containerized application
- **Redis & Celery (Optional)** – For background tasks
