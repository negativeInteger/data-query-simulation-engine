# Data Query Simulation Engine

## 📖 Overview
The **Data Query Simulation Engine** is a simple FastAPI-based service that processes natural language queries and translates them into structured pseudo-SQL queries with mock data. It supports:
- **Filtering** (`WHERE` conditions)
- **Sorting** (`ORDER BY`)
- **Aggregation** (`SUM() calculations`)
- **Query Explanation & Validation**
- **API Key Authentication**

## 🚀 Features
- Convert natural language queries into structured pseudo-SQL.
- Return mock data based on the query.
- Validate and explain queries before processing.
- Secure API access using API keys.
- Interactive API documentation with **Swagger UI** and **ReDoc**.

## 🏗️ Installation
```sh
# Clone the repository
git clone https://github.com/negativeInteger/data-query-simulation-engine.git
cd data-query-simulation-engine

# Install dependencies
uv pip install -r requirements.txt

# Run the FastAPI server
uvicorn app.main:app --host localhost --port 8000
```

## 🌐 API Documentation
Once the server is running, you can access interactive API documentation at:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🔑 API Key Authentication
Users must generate an API key before accessing protected endpoints. API keys are provided during **signup** and must be included in requests via headers:

### **1️⃣ User Signup (`POST /api/auth/signup`)**
Registers a new user and returns an API key.

#### 🔹 **Request**
```json
{
  "email": "user1@example.com",
}
```
#### 🔹 **Response**
```json
{
  "api_key": "abcd1234efgh5678abcd1234efgh5678"
}
```

### **2️⃣ Using API Key**
Include the API key in the request header:
```sh
curl -X POST "http://localhost:8000/api/query" \
     -H "Authorization: Bearer abcd1234efgh5678" \
     -H "Content-Type: application/json" \
     -d '{"query": "Get all transactions"}'
```

## 🌐 API Endpoints & Responses

### **3️⃣ Process Query (`POST /api/query`)**  
Convert a **natural language query** into a **pseudo-SQL query** and return mock data.  

#### 🔹 **Request**  
```json
{
  "query": "Get all transactions"
}
```
#### 🔹 **Response**  
```json
{
  "query": "SELECT * FROM transactions;",
  "data": [
    {"id": 101, "amount": 250, "status": "completed"},
    {"id": 102, "amount": 500, "status": "pending"}
  ]
}
```

---

### **4️⃣ Process Query with Filtering (`POST /api/query`)**  
Applies **WHERE** filtering based on user query.  

#### 🔹 **Request**  
```json
{
  "query": "Get all transactions where amount is greater than 300"
}
```
#### 🔹 **Response**  
```json
{
  "query": "SELECT * FROM transactions WHERE amount > 300;",
  "data": [
    {"id": 102, "amount": 500, "status": "pending"}
  ]
}
```

---

### **5️⃣ Process Query with Sorting (`POST /api/query`)**  
Applies **ORDER BY** sorting based on user query.  

#### 🔹 **Request**  
```json
{
  "query": "Sort sales by region in ascending order"
}
```
#### 🔹 **Response**  
```json
{
  "query": "SELECT * FROM sales ORDER BY region ASC;",
  "data": [
    {"id": 1, "region": "North", "revenue": 5000},
    {"id": 2, "region": "South", "revenue": 3000}
  ]
}
```

---

### **6️⃣ Process Query with Aggregation (`POST /api/query`)**  
Calculates **SUM()** for a numeric field.  

#### 🔹 **Request**  
```json
{
  "query": "What is the total revenue by sales?"
}
```
#### 🔹 **Response**  
```json
{
  "query": "SELECT SUM(revenue) FROM sales;",
  "data": [
    {"total": 8000}
  ]
}
```

---

### **7️⃣ Explain Query (`POST /api/explain`)**  
Breaks down a natural query into its components.  

#### 🔹 **Request**  
```json
{
  "query": "Get all transactions where amount is greater than 300"
}
```
#### 🔹 **Response**  
```json
{
  "action": "fetch",
  "table": "transactions",
  "filter": "amount greater than 300",
  "sort": null,
  "aggregation": null
}
```

---

### **8️⃣ Validate Query (`POST /api/validate`)**  
Checks if the query is referencing a supported dataset.  

#### 🔹 **Request**  
```json
{
  "query": "Get all customers"
}
```
#### 🔹 **Response**  
```json
{
  "valid": false
}
```

#### 🔹 **Request**  
```json
{
  "query": "Get all sales"
}
```
#### 🔹 **Response**  
```json
{
  "valid": true
}
```

## 📜 License
This project is open-source and available under the MIT License.
