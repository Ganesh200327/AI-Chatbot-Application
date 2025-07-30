# AI Chatbot using Django & Microsoft DialoGPT

This is an **AI-powered chatbot** built with the **Django framework** and **Hugging Face Transformers**.  
It uses the pre-trained **Microsoft DialoGPT-medium** model to generate human-like responses in real time and stores conversation history in a database.

---

## 🚀 Features
- 💬 Real-time AI-powered chatbot using **DialoGPT**
- 📦 Built with **Django** backend
- 🗄 Conversation history stored in **SQLite** (or any Django-supported DB)
- 🌐 Simple and responsive frontend UI
- ⚡ Hugging Face `transformers` integration

---

## 📂 Project Structure
```
ai_chatbot/
│
├── chatbot/ # Django app for chatbot
│   ├── migrations/ # Database migrations
│   ├── templates/ # HTML templates
│   │   └── chatbot/
│   │       └── chat.html
│   ├── models.py # Conversation model
│   ├── views.py # Chatbot logic
│   ├── urls.py # Routes
│
├── ai_chatbot/ # Main Django project settings
│   ├── settings.py
│   ├── urls.py
│
├── db.sqlite3 # SQLite database
├── manage.py # Django management script
├── requirements.txt # Python dependencies
└── README.md # Documentation
```

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ai-chatbot-django.git
cd ai-chatbot-django
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
**requirements.txt**
```
Django>=4.0
transformers>=4.20.0
torch>=1.9.0
```

### 4️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the Development Server
```bash
python manage.py runserver
```
Visit: [http://127.0.0.1:8000/chatbot/](http://127.0.0.1:8000/chatbot/)

---

## 🧠 How It Works

- Frontend (HTML + JavaScript) sends user messages via AJAX to the Django backend.
- Backend (Django) uses Hugging Face DialoGPT-medium to generate AI responses.
- The Conversation model saves the chat history in the database.
- The response is sent back to the frontend in JSON format.

---

## 📜 Example Conversation

> **User:** Hello!  
> **Bot:** Hi there! How are you doing today?
]
---
## 📌 Future Improvements

- Use larger language models for more context-aware responses.
- Add authentication to track user-specific conversations.
- Implement WebSocket for live streaming responses.
- Deploy on Heroku / Render / Railway with GPU-based inference.

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙌 Acknowledgements

- Django - Web Framework
- Hugging Face Transformers - NLP Models
- Microsoft DialoGPT - Pretrained Chat Model
