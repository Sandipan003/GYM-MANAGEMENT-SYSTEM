# 🏋️ KINETIC PULSE | Elite Performance Gym Management System

![KINETIC PULSE Banner](https://img.shields.io/badge/KINETIC-PULSE-d4fb00?style=for-the-badge&logoScale=0.5&labelColor=0e0e0e)
![Django](https://img.shields.io/badge/Django-4.2-092e20?style=for-the-badge&logo=django)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479a1?style=for-the-badge&logo=mysql&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.0-38bdf8?style=for-the-badge&logo=tailwind-css)

**KINETIC PULSE** is a high-end, professional-grade Gym Membership Management System built with **Django** and **MySQL**. Designed for elite performance facilities, it combines robust backend logic with a stunning, modern UI featuring glassmorphism and real-time analytics.

---

## ⚡ Core Features

### 🏢 Staff & Admin Panel
- **Real-time KPI Tracking**: Live active member counts, monthly revenue, and facility occupancy.
- **Revenue Velocity Chart**: Dynamic visual data representing the last 6 months of financial performance.
- **Member CRM**: Full profiles with attendance history, payment logs, and personal details.
- **Auto-generated IDs**: Professional member identification system (#KP-0001).

### 👤 Personalized Member Portal
- **Member Dashboard**: Personal performance metrics, calories burned estimation, and workout trends.
- **Secure Login**: Members can now log in using custom credentials set during enrollment.
- **Self-Service Upgrades**: Members can browse membership tiers and "pay" (simulated) to instantly activate their status and tier.
- **Live Check-in**: One-click "I am in the gym" logging directly from the member portal.

### 💳 Membership & Payments
- **Tiered Plans**: Flexible pricing models with custom features (Elite, Pro, Starter, etc.).
- **Automated Billing Status**: Members are switched to **ACTIVE** upon payment and auto-calculated expiry dates.
- **Transaction Ledger**: Detailed history stored in MySQL for full auditing.

---

## 🚀 Quick Setup

### 1. Prerequisites
- Python 3.8+
- MySQL Server (MAMP/XAMPP recommended)
- `PyMySQL` driver for Django

### 2. Database Backend (MySQL)
KINETIC PULSE is optimized for **MySQL 8.0**. Ensure your server is running (default port `8889` for MAMP).
1. Create a database named `kinetic_pulse_db` in **phpMyAdmin** or MySQL Shell.
2. The application will auto-initialize the schema upon the first migration.

### 3. Environment Configuration
Create a `.env` file in the root directory:
```env
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=kinetic_pulse_db
DB_USER=root
DB_PASSWORD=root
DB_HOST=localhost
DB_PORT=8889  # Default MAMP port
```

### 4. Installation
```bash
pip install -r requirements.txt
python manage.py migrate
```

### 5. Launch
```bash
python manage.py runserver
```

---

## 🔐 Credentials (Demo)
Access the dashboard at `http://127.0.0.1:8000/`

- **Staff Account**: `admin` / `admin123`
- **Member Account**: `mysqluser123` / `password123`

---

## 🎨 Tech Stack
- **Backend**: Django 4.2 & PyMySQL
- **Database**: MySQL 8.0 (viewable via phpMyAdmin)
- **Frontend**: Vanilla HTML/JS, Tailwind CSS (CDN)
- **Design**: Glassmorphism aesthetic with Lexend & Inter typography

---

© 2024 Kinetic Pulse Systems. All Rights Reserved.
