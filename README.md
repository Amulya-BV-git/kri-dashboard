#  KRI Dashboard Backend

---

##  Overview

This project is an AI-powered backend service built using Flask.
It is part of the **KRI (Key Risk Indicator) Dashboard** and provides intelligent risk analysis using AI.

The system processes user inputs and generates:

* Risk descriptions
* Recommendations
* Structured reports
* Document insights
* Batch analysis
* Knowledge retrieval (RAG)

---

##  Features

* 🔹 AI Risk Description
* 🔹 AI Recommendations
* 🔹 Report Generation (Async + Structured Output)
* 🔹 Document Analysis (Insights + Risks)
* 🔹 Batch Processing (Multiple Inputs)
* 🔹 RAG (Retrieval-Augmented Generation using ChromaDB)
* 🔹 Streaming Support (SSE)
* 🔹 Modular Architecture (Routes + Services)

---

## Prerequisites

* Python 3.10+
* pip installed
* Internet connection (for Groq API)
* Git (optional)

---

##  Installation

```bash
git clone https://github.com/chaithanya-v-28/kri-dashboard.git
cd kri-dashboard/ai-service
pip install flask flask-cors python-dotenv requests chromadb sentence-transformers
```

---

##  Environment Variables

Create a `.env` file inside `ai-service`:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

##  Run the Server

```bash
python app.py
```

Server runs at:

```
http://127.0.0.1:5555/
```



##  API Endpoints

---

### 1. Describe Risk

**POST** `/describe`

**Request**

```json
{
  "text": "Cybersecurity risk"
}
```

**Response**

```json
{
  "title": "Cybersecurity Risk",
  "description": "Cybersecurity risks involve threats to systems, networks, and data.",
  "risk_level": "Medium",
  "generated_at": "timestamp"
}
```


### 2. Recommend

**POST** `/recommend`

**Request**

```json
{
  "text": "Cybersecurity risk"
}
```

**Response**

```json
{
  "input": "Cybersecurity risk",
  "recommendations": "Enable multi-factor authentication, update systems regularly, and monitor network activity."
}
```


### 3. Generate Report

**POST** `/generate-report`

**Request**

```json
{
  "text": "Cybersecurity risk"
}
```

**Response**

```json
{
  "title": "Cybersecurity Risk Analysis Report",
  "executive_summary": "...",
  "overview": "...",
  "top_items": [
    "Weak authentication",
    "Unpatched software",
    "Lack of monitoring"
  ],
  "recommendations": [
    {"action": "Enable MFA", "priority": "High"}
  ],
  "generated_at": "timestamp"
}
```


### 4. Analyse Document

**POST** `/analyse-document`

**Request**

```json
{
  "text": "System lacks encryption"
}
```

**Response**

```json
{
  "input": "System lacks encryption",
  "findings": [
    {"type": "insight", "description": "Sensitive data is exposed"},
    {"type": "risk", "description": "High chance of data breach"}
  ],
  "generated_at": "timestamp"
}
```



### 5. Batch Process

**POST** `/batch-process`

**Request**

```json
{
  "items": ["risk1", "risk2"]
}
```

**Response**

```json
{
  "count": 2,
  "results": [
    {"input": "risk1", "output": "..."},
    {"input": "risk2", "output": "..."}
  ]
}
```


### 6. RAG Query

**POST** `/rag`

**Request**

```json
{
  "query": "cybersecurity"
}
```

**Response**

```json
{
  "query": "cybersecurity",
  "results": [
    "Cybersecurity risks include phishing, malware, and data breaches."
  ]
}


## Performance & Optimization

* Preloaded embedding model for faster responses
* Optional Redis caching
* Reduced prompt size for efficiency
* Streaming support for real-time responses


## Testing

Run tests:

bash
pytest


## Status

✔ APIs implemented
✔ Async processing working
✔ Streaming enabled
✔ Batch processing added
✔ Unit tests completed
✔ Demo ready


## Future Improvements

* Add database (PostgreSQL / MongoDB)
* Add authentication (JWT)
* Build React frontend dashboard
* Improve AI prompt quality
* Enable Redis caching fully
* Deploy to cloud (AWS / Render)


## Author

Chaithanya V
AI Developer Intern


## Conclusion

This project demonstrates how AI can be integrated into backend systems to provide real-time risk analysis, intelligent recommendations, and structured reporting.



> **Tool-08 | Java Developer 2 | Spring Boot 3.2 | PostgreSQL | Redis | JWT**

A comprehensive **Key Risk Indicator (KRI) Dashboard** REST API built with Spring Boot, featuring JWT authentication, Redis caching, email notifications, AOP audit logging, and Flyway database migrations.

---

## 📋 Project Overview

| Property       | Value                          |
|----------------|--------------------------------|
| Developer      | Varad (Java Developer 2)       |
| Branch         | `varad-java-dev2`              |
| Framework      | Spring Boot 3.2.5              |
| Java Version   | Java 17                        |
| Database       | PostgreSQL                     |
| Cache          | Redis                          |
| Auth           | JWT (JJWT 0.12.5)              |
| Docs           | Swagger / OpenAPI 3            |
| Migration      | Flyway                         |

---

## 🗓️ Development Timeline

| Day   | Task                                      | Status |
|-------|-------------------------------------------|--------|
| Day 1 | Project setup, Flyway V1 migration (`kri` table), base structure | ✅ Done |
| Day 2 | Entity layer, Repository, DTOs, Exception handling | ✅ Done |
| Day 3 | Service layer (KriService), REST Controller, Swagger config | ✅ Done |
| Day 4 | JWT Security — UserEntity, AuthController, SecurityConfig | ✅ Done |
| Day 5 | Redis caching, Email alerts, Thymeleaf template, Scheduler | ✅ Done |
| Day 6 | AOP Audit logging, Unit tests, README, final polish | ✅ Done |
| Day 7 | Pagination & Filtering, CSV Export, Actuator endpoints | ✅ Done |
| Day 8 | Integration Tests (MockMvc), Dockerfile, docker-compose | ✅ Done |
| Day 9 | Role-Based Access Control (RBAC), Admin Controller | ✅ Done |
| Day 10 | Dashboard Analytics API, KRI statistics summary | ✅ Done |
| Day 11 | GitHub Actions CI/CD Pipeline, CONTRIBUTING.md | ✅ Done |
| Day 12 | KRI Audit History (kri_history table, V5 migration, history API) | ✅ Done |
| Day 13 | Rate Limiting (Bucket4j), ApiResponse<T> wrapper | ✅ Done |
| Day 14 | Soft Delete, Production profile, Custom Health Indicator (V6 migration) | ✅ Done |
| Day 15 | DashboardService unit tests, Request logging filter, Final cleanup | ✅ Done |
| Day 16 | In-app Notifications System (V7 migration, Notification entity, Auto-alerts) | ✅ Done |
| Day 17 | Excel Export using Apache POI | ✅ Done |
| Day 18 | Bulk Operations (Bulk Create & Bulk Status Update) | ✅ Done |
| Day 19 | Security hardening (CORS config, Security headers, Method security) | ✅ Done |

---

## 🏗️ Project Structure

```
backend/
└── src/main/java/com/internship/tool/
    ├── ToolApplication.java        # Entry point
    ├── config/
    │   ├── SecurityConfig.java     # Spring Security + JWT
    │   ├── JwtAuthFilter.java      # JWT request filter
    │   ├── OpenApiConfig.java      # Swagger UI config
    │   ├── RedisConfig.java        # Redis cache manager
    │   └── AuditAspect.java        # AOP audit logging
    ├── controller/
    │   ├── KriController.java      # KRI CRUD endpoints
    │   └── AuthController.java     # Register / Login endpoints
    ├── dto/
    │   ├── KriRequest.java         # KRI create/update body
    │   ├── KriResponse.java        # KRI response body
    │   ├── AuthRequest.java        # Login request
    │   ├── AuthResponse.java       # JWT token response
    │   └── RegisterRequest.java    # Registration request
    ├── entity/
    │   ├── AuditableEntity.java    # Base audit timestamps
    │   ├── Kri.java                # KRI JPA entity
    │   ├── User.java               # User JPA entity
    │   └── Role.java               # Role enum
    ├── exception/
    │   ├── GlobalExceptionHandler.java
    │   ├── ResourceNotFoundException.java
    │   └── ErrorResponse.java
    ├── repository/
    │   ├── KriRepository.java
    │   └── UserRepository.java
    ├── scheduler/
    │   └── KriScheduler.java       # Daily breach check + hourly stats
    └── service/
        ├── KriService.java
        ├── UserService.java
        ├── EmailService.java
        ├── JwtService.java
        └── impl/
            ├── KriServiceImpl.java
            ├── UserServiceImpl.java
            └── EmailServiceImpl.java
```

---

## 🚀 API Endpoints

### 🔐 Authentication
| Method | Endpoint                  | Description        | Auth Required |
|--------|---------------------------|--------------------|---------------|
| POST   | `/api/v1/auth/register`   | Register new user  | ❌ No         |
| POST   | `/api/v1/auth/login`      | Login, get JWT     | ❌ No         |

### 📊 KRI Management
| Method | Endpoint                     | Description                  | Auth Required |
|--------|------------------------------|------------------------------|---------------|
| POST   | `/api/v1/kri`                | Create new KRI               | ✅ Yes (ADMIN)|
| GET    | `/api/v1/kri`                | Get all KRIs                 | ✅ Yes        |
| GET    | `/api/v1/kri/{id}`           | Get KRI by ID                | ✅ Yes        |
| GET    | `/api/v1/kri/status/{status}`| Get KRIs by status           | ✅ Yes        |
| GET    | `/api/v1/kri/at-risk`        | Get BREACH/NEAR_BREACH KRIs  | ✅ Yes        |
| GET    | `/api/v1/kri/search`         | Paginated & filtered search  | ✅ Yes        |
| PUT    | `/api/v1/kri/{id}`           | Update KRI                   | ✅ Yes (ADMIN)|
| DELETE | `/api/v1/kri/{id}`           | Delete KRI                   | ✅ Yes (ADMIN)|
| GET    | `/api/v1/kri/export/csv`     | Export KRIs to CSV           | ✅ Yes        |
| GET    | `/api/v1/kri/export/excel`   | Export KRIs to Excel         | ✅ Yes        |
| POST   | `/api/v1/kri/bulk`           | Bulk create KRIs             | ✅ Yes (ADMIN)|
| PATCH  | `/api/v1/kri/bulk/status`    | Bulk update KRI statuses     | ✅ Yes (ADMIN)|
| PATCH  | `/api/v1/kri/{id}/archive`   | Soft-delete a KRI            | ✅ Yes (ADMIN)|
| GET    | `/api/v1/kri/{id}/history`   | Get audit history of a KRI   | ✅ Yes        |

### 🔔 In-App Notifications
| Method | Endpoint                            | Description                  | Auth Required |
|--------|-------------------------------------|------------------------------|---------------|
| GET    | `/api/v1/notifications`             | Get all notifications        | ✅ Yes        |
| GET    | `/api/v1/notifications/unread`      | Get unread notifications     | ✅ Yes        |
| GET    | `/api/v1/notifications/unread/count`| Get unread count             | ✅ Yes        |
| PATCH  | `/api/v1/notifications/{id}/read`   | Mark notification as read    | ✅ Yes        |
| PATCH  | `/api/v1/notifications/read-all`    | Mark all as read             | ✅ Yes        |

### 📈 Analytics & Dashboard
| Method | Endpoint                     | Description                  | Auth Required |
|--------|------------------------------|------------------------------|---------------|
| GET    | `/api/v1/dashboard/summary`  | Get full KRI statistics      | ✅ Yes        |

### 👨‍💼 Admin Management
| Method | Endpoint                     | Description                  | Auth Required |
|--------|------------------------------|------------------------------|---------------|
| GET    | `/api/v1/admin/users`        | List all users               | ✅ Yes (ADMIN)|
| GET    | `/api/v1/admin/users/{id}`   | Get user details             | ✅ Yes (ADMIN)|
| PATCH  | `/api/v1/admin/users/{id}/promote` | Promote to ADMIN       | ✅ Yes (ADMIN)|
| PATCH  | `/api/v1/admin/users/{id}/demote`  | Demote to USER         | ✅ Yes (ADMIN)|
| DELETE | `/api/v1/admin/users/{id}`   | Delete user account          | ✅ Yes (ADMIN)|

---

## ⚙️ Setup & Run

### Prerequisites
- Java 17+
- PostgreSQL 15+
- Redis 7+
- Maven 3.8+

### 1. Clone the repository
```bash
git clone https://github.com/varadsure362-cmyk/kri-dashboard.git
cd kri-dashboard/backend
```

### 2. Configure environment variables
Copy `.env.example` to `.env` and fill in your values:
```env
DB_USERNAME=postgres
DB_PASSWORD=yourpassword
JWT_SECRET=your-base64-secret
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

### 3. Create PostgreSQL database
```sql
CREATE DATABASE kri_db;
```

### 4. Run the application
```bash
mvn spring-boot:run
```

### 5. Access Swagger UI
```
http://localhost:8080/swagger-ui.html
```

---

## 🔑 Authentication Flow

1. **Register** → `POST /api/v1/auth/register`
2. **Login** → `POST /api/v1/auth/login` → receive JWT token
3. **Use token** → Add `Authorization: Bearer <token>` header to all protected requests

---

## 🧪 Running Tests

```bash
mvn test
```

---

## 📦 Key Dependencies

| Dependency         | Purpose                      |
|--------------------|------------------------------|
| Spring Boot 3.2.5  | Core framework               |
| Spring Data JPA    | ORM / database access        |
| PostgreSQL Driver  | Database connectivity        |
| Flyway             | Database migrations          |
| Spring Security    | Authentication & authorization|
| JJWT 0.12.5        | JWT token generation         |
| Spring Data Redis  | Caching layer                |
| Spring Mail        | Email notifications          |
| Thymeleaf          | Email templates              |
| SpringDoc OpenAPI  | Swagger UI                   |
| Lombok             | Boilerplate reduction        |
| Spring AOP         | Audit logging                |
| JaCoCo             | Code coverage reports        |
