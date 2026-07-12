# Enterprise Management System (EMS)

A scalable **Enterprise Management System API** built using **FastAPI, SQLAlchemy, MySQL, JWT Authentication, and Role-Based Access Control (RBAC)**.

This project is designed with a modular enterprise architecture supporting multiple business operations such as user management, company structure, employees, customers, vendors, products, inventory, sales, finance, workflow automation, notifications, reporting, and dashboards.

---

## 🚀 Tech Stack

### Backend

* Python 3.14
* FastAPI
* SQLAlchemy ORM
* Pydantic
* MySQL
* Alembic (Database Migration)
* JWT Authentication
* bcrypt Password Hashing

### Testing

* Pytest
* FastAPI TestClient
* Coverage Testing

### Development Tools

* VS Code
* MySQL Workbench
* Git & GitHub

---

# 📌 Features

## 🔐 Authentication & Security

* User Registration
* Login Authentication
* JWT Access Tokens
* Refresh Token Support
* OTP Based MFA Flow
* Forgot Password
* Reset Password
* Password Hashing
* Secure Middleware Headers

---

## 👥 User & Organization Management

### Users

* User CRUD operations
* Dynamic role management
* Permission-based authorization

### Organization Structure

* Companies
* Branches
* Departments
* Teams
* Employee assignment

---

## 🔑 Dynamic Role-Based Access Control (RBAC)

The system uses a dynamic permission architecture:

```
Role
 |
 |-- Role Permissions
          |
          |-- Resource
          |
          |-- Permission
```

Example:

```
Admin
 ├── Company
 │     ├── Create
 │     ├── View
 │     └── Delete
 │
 ├── Product
 │     ├── Create
 │     └── View
```

Authorization is handled using:

```
require_permission(resource, action)
```

---

# 🏢 Business Modules

## Customer Management

* Customer profiles
* Customer information management

## Employee Management

* Employee profiles
* Attendance
* Leave management
* Payroll
* Performance reviews

## Vendor Management

* Vendor records
* Supplier information

## Product Management

* Products
* Categories
* Product attributes
* Pricing

## Inventory Management

* Stock tracking
* Inventory operations
* Low stock monitoring

## Purchase Management

* Purchase orders
* Goods receipt management

## Sales Management

* Sales orders
* Customer transactions

## Shipping Management

* Shipment tracking

## Finance Module

* General Ledger
* Accounts Payable
* Accounts Receivable
* Financial Reports
* Trial Balance
* Profit & Loss
* Balance Sheet

---

# 📊 Enterprise Features

## Dashboard

* Executive dashboard
* Operational dashboard
* Customer analytics
* Employee growth charts
* Inventory status
* Sales forecasting

## Workflow System

* Approval workflows
* Pending approvals

## Notifications

* Notification management
* Webhook support

## Document Management

* File upload support

## Search

* Enterprise search functionality

## Reporting

* Business reports
* Data summaries

---

# 📂 Project Structure

```
enterprise_EMS/

│
├── core/
│   ├── config.py
│   ├── security.py
│   └── exceptions/
│
├── routers/
│   ├── auth.py
│   ├── company.py
│   ├── employee.py
│   ├── product.py
│   └── ...
│
├── services/
│
├── repositories/
│
├── models/
│
├── schemas/
│
├── dependencies/
│
├── middleware/
│
├── migrations/
│
├── tests/
│
├── database.py
├── main.py
└── requirements.txt
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Bhaavanineeluri/enterprise_ems.git
```

Navigate into the project:

```bash
cd enterprise_ems
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🗄️ Database Setup

Create MySQL database:

```sql
CREATE DATABASE enterprise_ems;
```

Configure environment variables:

Create:

```
.env
```

Example:

```
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/enterprise_ems

SECRET_KEY=your_secret_key

ALGORITHM=HS256
```

Run migrations:

```bash
alembic upgrade head
```

---

# ▶️ Run Application

Start FastAPI server:

```bash
uvicorn main:app --reload
```

API will run at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# 🧪 Running Tests

Run all tests:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov
```

---

# 🔄 API Versioning

All APIs use:

```
/api/v1
```

Example:

```
GET /api/v1/products/
POST /api/v1/customers/
GET /api/v1/dashboard/
```

---

# 🔒 Security Practices

* JWT Authentication
* Password hashing using bcrypt
* Permission-based authorization
* Company-level data isolation
* Exception handling middleware
* Secure headers middleware

---

# 📈 Future Improvements

* Redis caching
* Background task processing
* Docker deployment
* CI/CD pipeline improvements
* Cloud deployment
* Advanced analytics
* Unit test expansion

---

# 👩‍💻 Author

**Bhaavani Neeluri**

Backend Developer
FastAPI | Python | SQL | MySQL

---

# 📄 License

This project is developed for learning and enterprise backend architecture practice.
