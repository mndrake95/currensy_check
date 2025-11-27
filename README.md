<div align="center">

# 💰 USD Exchange Rate Service

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Django](https://img.shields.io/badge/django-5.2-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

**A robust Django microservice for tracking real-time USD/RUB exchange rates.**
<br>
Features smart throttling, request history, and a dual JSON/HTML interface.

[Features](#-features) • [Tech Stack](#-tech-stack) • [Installation](#-installation--setup) • [Decomposition](#-task-decomposition)

</div>

---

## 📋 Features

* **⚡ External API Integration**
    Fetches accurate rates from `exchangerate-api.com`.
* **🛡️ Smart Throttling**
    Prevents API spam by limiting updates to once every **10 seconds** (Global cache).
* **🖱️ On-Demand Updates**
    * **Browser:** Passive viewing (cached data).
    * **Button:** Interactive AJAX update mechanism via "Update Rate" button.
* **📜 History Tracking**
    Automatically stores and displays the last **10 records**.
* **🔌 Dual Interface (Content Negotiation)**
    * `JSON`: For API clients (Postman, curl).
    * `HTML`: For human users (Dashboard).

---

## 🛠 Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Core** | ![Python](https://img.shields.io/badge/-Python_3.11-blue) | Backend logic |
| **Framework** | ![Django](https://img.shields.io/badge/-Django_5.2-092E20) | Web framework & ORM |
| **Database** | ![SQLite](https://img.shields.io/badge/-SQLite-003B57) | Lightweight storage |
| **Frontend** | ![JS](https://img.shields.io/badge/-JavaScript-F7DF1E) | AJAX updates (Vanilla JS) |

---

## 📂 Project Structure

```text
currensy_check/
├── usd_check/           # Main App
│   ├── migrations/      # DB Migrations
│   ├── templates/       # HTML (index.html)
│   ├── admin.py         # Admin panel config
│   ├── models.py        # Database models
│   └── views.py         # Business logic & API
├── test_site/           # Project Settings
├── manage.py            # CLI entry point
└── requirements.txt     # Dependencies
