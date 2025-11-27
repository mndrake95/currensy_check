<div align="center">

# 💰 USD Exchange Rate Service

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Django](https://img.shields.io/badge/django-5.2-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

**A robust Django microservice for tracking real-time USD/RUB exchange rates.**
<br>
Features smart throttling, request history, and a dual JSON/HTML interface.


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

-----

## 🚀 Installation & Setup

Follow these steps to deploy the service locally.

### 1\. Clone & Prepare

Get the code and navigate to the project directory:

```bash
git clone [https://github.com/mndrake95/currensy_check.git](https://github.com/mndrake95/currensy_check.git)
cd currensy_check
```

### 2\. Environment Setup

Create a virtual environment to isolate dependencies:

**🪟 Windows:**

```powershell
python -m venv venv
.\venv\Scripts\activate
```

**🐧 Linux /  macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3\. Dependencies & Database

Install required packages and apply database migrations:

```bash
pip install -r requirements.txt
python manage.py migrate
```

### 4\. Launch

Start the development server:

```bash
python manage.py runserver
```

> **🎉 Success\!** The service is now live at:
> **[http://127.0.0.1:8000/get-current-usd/](https://www.google.com/search?q=http://127.0.0.1:8000/get-current-usd/)**

-----

## 🔨 Task Decomposition

The development lifecycle was divided into **6 key stages**, ensuring a structured approach:

  - [x] **📦 Project Initialization**
      - Environment setup (`venv`, `git`).
      - Django project structure creation.
  - [x] **🗄️ Database Design**
      - `ExchangeRate` model implementation.
      - Admin panel configuration for monitoring.
  - [x] **🧠 Core Business Logic**
      - Integration with `exchangerate-api.com`.
      - **Throttling logic** (10s cooldown implementation).
  - [x] **🔌 API & Views**
      - Unified endpoint creation.
      - Content negotiation logic (JSON vs HTML).
  - [x] **🎨 Frontend Interaction**
      - HTML Template with data table.
      - **AJAX** implementation for the "Update" button.
  - [x] **✨ Final Polish**
      - Error handling & edge cases.
      - Documentation & Refactoring.

-----

## ⏱ Timings (Plan vs Fact)

Detailed breakdown of time expenditure for each component.

| Phase | Estimate (h) | Actual (h) | Notes |
| :--- | :---: | :---: | :--- |
| **Project Setup** | 0.5 | 0.5 | Git init, Venv, Django start |
| **Models & DB** | 0.5 | 0.5 | Schema design & Migrations |
| **Core Logic** | 1.5 | 2.5 | API integration & Throttling |
| **Frontend & UI** | 1.0 | 2.0 | Added AJAX Button & Styling |
| **Docs & Polish** | 0.5 | 0.5 | README, Cleanup |
| **TOTAL** | **4.0** | **6.0** | *Added extra frontend features* |

-----
