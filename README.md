# 🔐 SecureByte — Advanced Password Generator

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

**“Small Bytes, Big Security.”**

A secure and customizable password generator with a modern web interface and a Python backend. **SecureByte** helps users generate strong, random, and reliable passwords instantly.


## 📁 Project Structure

SecureByte/
│── Backend/            # Flask API for password generation logic
│   │── logic.py        # Core generation engine
│   └── requirements.txt
└── index.html          # Main Frontend interface (Root level)

---

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/shreeharsh-patil/SecureByte.git
cd SecureByte
```

### 2. Install Dependencies

```bash
pip install -r Backend/requirements.txt
```

### 3. Run the Backend Server

```bash
python Backend/logic.py
```

### 4. Open the Frontend

Open `index.html` in your browser.

---

## ✨ Features

* 🔑 Customizable password length (8–64 characters)
* 🔠 Include/exclude uppercase letters
* 🔢 Include/exclude numbers
* 🔣 Include/exclude special symbols
* 🛡️ Real-time password strength meter
* ⚡ Instant generation (Backend + Local fallback)
* 📋 Copy to clipboard functionality
* 🌙 Modern dark theme with glassmorphism UI

---

## ⚙️ How It Works

* The backend (Flask) generates secure passwords using `secrets` module for cryptographically strong entropy.
* The frontend (HTML/CSS/JS) communicates with the backend and provides a seamless UI.
* **Fallback Mode:** If the backend is unreachable, SecureByte switches to local `window.crypto` generation to ensure zero downtime.

---

## 📡 API Documentation

SecureByte provides a simple REST API:
- `GET /generate?length=32&upper=true&numbers=true&symbols=true`
- `GET /health`

---

## 🚀 Future Improvements

* 💾 Save password history locally (IndexedDB)
* 🌐 Deploy as a live web application
* 👤 Add user authentication
* 📱 Progressive Web App (PWA) support

---

## 🧑‍💻 Author

Developed by **Shreeharsh Patil**

GitHub: [shreeharsh-patil](https://github.com/shreeharsh-patil)

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
