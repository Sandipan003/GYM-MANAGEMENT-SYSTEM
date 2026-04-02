# 🏋️ KINETIC PULSE | Elite Performance Gym Management System

![KINETIC PULSE Banner](https://img.shields.io/badge/KINETIC-PULSE-d4fb00?style=for-the-badge&logoScale=0.5&labelColor=0e0e0e)
![Django](https://img.shields.io/badge/Django-4.2-092e20?style=for-the-badge&logo=django)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479a1?style=for-the-badge&logo=mysql&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.0-38bdf8?style=for-the-badge&logo=tailwind-css)

**KINETIC PULSE** is a high-end, professional-grade Gym Membership Management System built with **Django** and **MySQL**. Designed for elite performance facilities, it combines robust backend logic with a stunning, modern UI featuring glassmorphism and real-time analytics.

---

## ⚡ Core Features

### 📊 Elite Dashboard
- **Real-time KPI Tracking**: Live active member counts, monthly revenue, and facility occupancy.
- **Revenue Velocity Chart**: Dynamic visual data representing the last 6 months of financial performance.
- **Live Activity Feed**: Instantly view member check-ins and gym zone activity.

### 👤 Member Management
- **Full CRM**: Comprehensive profiles with attendance history, payment logs, and personal details.
- **Smart Filtering**: Find members by status (Active, Expired, Pending) or specific membership plans.
- **Auto-generated IDs**: Professional member identification system (#KP-0001).

### 💳 Membership & Payments
- **Tiered Plans**: Flexible pricing models with custom features and durations.
- **Automated Billing Status**: Members are automatically activated upon payment and expired once their term ends.
- **Transaction Ledger**: Detailed history of all financial activities including multiple payment methods (UPI, Card, Cash).

### 📈 Attendance Analytics
- **Peak Hours Heatmap**: Identify facility usage patterns to optimize staff and equipment.
- **Member Engagement**: Analytics on daily vs. weekly vs. occasional visitors.
- **Live Check-in Tool**: Simple entry logging with automatic checkout management.

---

## 🚀 Quick Setup

### 1. Prerequisites
- Python 3.8+
- MySQL Server (MAMP/XAMPP recommended)

### 2. Database Setup
1. Create a MySQL database named `kinetic_pulse_db`.
2. Import the provided `database_setup.sql` file:
   ```bash
   mysql -u root -p kinetic_pulse_db < database_setup.sql
   ```

### 3. Environment Configuration
Create a `.env` file in the root directory with the following:
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
python3 manage.py runserver
```

---

## 🔐 Credentials (Demo)
Access the dashboard at `http://127.0.0.1:8000/`

- **Username**: `admin`
- **Password**: `admin123`

---

## 🎨 Tech Stack
- **Backend**: Django 4.2 & PyMySQL
- **Database**: MySQL 8.0
- **Frontend**: Vanilla HTML/JS, Tailwind CSS (CDN)
- **Icons**: Material Symbols by Google
- **Typography**: Lexend & Inter

---

© 2024 Kinetic Pulse Systems. All Rights Reserved.
