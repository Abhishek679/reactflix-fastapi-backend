# 🎬 ReactFlix FastAPI Backend

This is the backend service for the **ReactFlix** subscription-based streaming application. It handles **user authentication**, **movie data processing**, and **GPT-powered movie suggestions** using FastAPI.

> 🧱 Built with: Python · FastAPI · JWT · TMDB API · GPT

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Abhishek679/reactflix-fastapi-backend.git
cd reactflix-fastapi-backend
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Unix
venv\Scripts\activate   # For Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory:

```env
JWT_SECRET_KEY=your_secret_key
TMDB_API_KEY=your_tmdb_api_key
GPT_API_KEY=your_openai_api_key
```

### 5. Start the server
```bash
uvicorn app.main:app --reload
```

---

## 🧠 Features

- ✅ **User Authentication**
  - Sign In / Sign Up APIs
  - JWT token-based session management

- 🎬 **TMDB Integration**
  - Fetch now playing movies
  - Get movie trailers and metadata

- 🤖 **GPT-Powered Movie Suggestions**
  - GPT API-based suggestions based on user input
  - Search-related movie discovery

- 🔐 **Protected Endpoints**
  - Use JWT middleware to secure routes

---

## 📁 Project Structure

```
.
├── main.py
├── routers/
│   ├── auth.py
│   ├── user.py
│   └── movies.py
├── services/
│   ├── tmdb_service.py
│   └── gpt_service.py
├── models/
│   └── user.py
├── utils/
│   ├── auth.py
│   └── jwt_handler.py
├── crud.py
├── database.py
├── main.py
├── .env.example
└── requirements.txt
```

---

## 🔌 API Endpoints

| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| POST   | /auth/signup     | Create user              |
| POST   | /auth/login      | Authenticate user        |
| GET    | /movies/now      | Get now playing movies   |
| POST   | /movies/gpt      | Get GPT movie suggestions|

---

## 📃 License

MIT License

---

## 🙋‍♂️ Author

Made with ❤️ by [Your Name](https://github.com/Abhishek679)
