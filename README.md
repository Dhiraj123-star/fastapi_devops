# ✅ FastAPI Task Manager

A lightweight **Task Manager API** built using **FastAPI** and ready for **production** with:

- 🚀 GitHub Actions for CI/CD  
- 🐳 Docker support  
- ☸️ Kubernetes deployment  
- 🌐 Ingress via NGINX

---

## 🔧 Features

- 📥 Add new tasks
- 📋 List all tasks
- ✏️ Update tasks
- 🗑️ Delete tasks
- 🆔 Auto-incrementing Task IDs
- 🛠️ Built-in memory-based storage (great for POCs & demos)

---

## 📦 API Endpoints

| Method | Endpoint            | Description                  |
|--------|---------------------|------------------------------|
| GET    | `/`                 | Welcome message              |
| GET    | `/tasks`            | Fetch all tasks              |
| POST   | `/tasks`            | Add a new task               |
| PUT    | `/tasks/{task_id}`  | Update a task by ID          |
| DELETE | `/tasks/{task_id}`  | Delete a task by ID          |

---

## 📁 Sample Task Payload

```json
{
  "title": "Finish writing README",
  "description": "Explain endpoints and setup"
}
