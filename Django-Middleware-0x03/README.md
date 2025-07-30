# Messaging App 📩

A simple messaging API built with Django and Django REST Framework. This project supports conversations and messages between users and is designed for learning purposes as part of the ALX Backend specialization.

---

## 🚀 Features

- Create and list conversations
- Send and retrieve messages
- RESTful API with JSON responses
- Organized using Django ViewSets
- Supports custom user models

---

## 📁 Project Structure

```bash
messaging_app/
├── chats/                  # Django app for conversations and messages
│   ├── models.py           # Message and Conversation models
│   ├── views.py            # ViewSets for API endpoints
│   ├── serializers.py      # DRF serializers
│   └── urls.py             # App-level URLs
├── messaging_app/
│   └── settings.py         # Django project settings
├── manage.py
├── requirements.txt
└── README.md


##To install dependencies
>pip install -r requirements.txt
