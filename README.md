# 🌐 FastAPI JSON Backend Project

A super-simplified backend system using **FastAPI** and **Uvicorn**, designed to demonstrate JSON data handling, validation with Pydantic, and a simple HTML frontend for interacting with your API.

---

## 🚀 Features

- 🏠 **Root endpoint (`/`)**: Loads a simple webpage
- 📤 **Send JSON (`/get-json`)**: Returns sample JSON data
- 📥 **Receive JSON (`/receive-json`)**: Accepts JSON and stores it locally
- ✅ **Data validation**: Uses Pydantic `BaseModel` to ensure input format
- 💾 **Local storage**: Data saved to `storage/data.json`
- 🧪 **Bonus HTML page**: Allows you to view and send data without Postman

---

## 🔧 Setup Instructions

### 1. Clone or download this repo
```bash
git clone https://github.com/your-username/fastapi-json-backend.git
cd fastapi-json-backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
Open your browser and visit:

📄 Main Page: http://localhost:8000

📘 API Docs: http://localhost:8000/docs

| Endpoint        | Method | Description                               |
| --------------- | ------ | ----------------------------------------- |
| `/`             | GET    | Serves HTML form                          |
| `/get-json`     | GET    | Returns sample JSON data                  |
| `/receive-json` | POST   | Accepts and validates JSON, saves to file |
| `/data`         | GET    | Returns all stored JSON data              |


## 📦 Tech Stack
FastAPI – modern Python web framework

Uvicorn – lightning-fast ASGI server

Pydantic – data validation and parsing

Jinja2 – for rendering HTML

HTML/JS – frontend interface

## 🌐 Live Webiste
Main page : http://103.179.44.192:8000/
Api Docs : http://103.179.44.192:8000/docs
