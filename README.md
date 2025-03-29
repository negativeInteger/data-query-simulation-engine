# 🧠 Data Query Simulation Engine

🚀 A lightweight backend service that simulates an AI-powered **natural language data query system**, converting simple text queries into pseudo-SQL and returning mock responses.

## 📌 Features
- ✅ Accepts **natural language queries** and converts them to pseudo-SQL.
- ✅ Provides an **explanation of the query** structure.
- ✅ Validates the feasibility of a given query.
- ✅ Implements **lightweight authentication** via API key.
- ✅ Proper **error handling** and structured API responses.

---

## 📂 Project Structure

```
📦 data-query-simulation-engine
│── 📂 app
│   ├── main.py             # FastAPI application
│   ├── database.py         # Mock database connection
│   ├── query_processor.py  # Converts text queries to pseudo-SQL
│   ├── auth.py             # API key authentication middleware
│   ├── routes.py           # API routes
│── 📂 tests
│   ├── test_api.py         # API endpoint test cases
│── requirements.txt        # Dependencies
│── README.md               # Documentation
│── .gitignore              # Git ignore file
```

---

## 🚀 **Setup Instructions**
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/mini-data-query-engine.git
cd mini-data-query-engine
```

### 2️⃣ **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Run the FastAPI Server**
```bash
uvicorn app.main:app --reload
```

### 5️⃣ **Access API Documentation (Swagger UI)**
- Open: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📌 **API Endpoints**
### 1️⃣ **POST `/query`** → Convert natural language query to pseudo-SQL  
**Request:**
```json
{
  "query": "Show me total sales for the last month"
}
```
**Response:**
```json
{
  "query": "SELECT SUM(sales) FROM sales_data WHERE date >= '2024-02-01'",
  "result": 125000
}
```

### 2️⃣ **POST `/explain`** → Explain query structure  
**Request:**
```json
{
  "query": "Get the top 5 best-selling products"
}
```
**Response:**
```json
{
  "query": "SELECT product_name, SUM(quantity) AS total_sold FROM sales_data GROUP BY product_name ORDER BY total_sold DESC LIMIT 5",
  "explanation": "Retrieves the top 5 products based on sales volume."
}
```

### 3️⃣ **POST `/validate`** → Validate query feasibility  
**Request:**
```json
{
  "query": "Find the total revenue by region"
}
```
**Response:**
```json
{
  "query": "SELECT region, SUM(revenue) FROM sales_data GROUP BY region",
  "valid": true,
  "reason": "Query is valid and can be executed."
}
```

### 4️⃣ **Authentication**
Add API Key in the request header:
```http
X-API-KEY: mysecureapikey
```

---

## ✅ **Running Tests**
```bash
pytest tests/
```

---

## 🌍 **Deployment on Render**
1. **Push code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```
2. **Go to [Render](https://render.com/)**
3. **Create a new Web Service**
4. **Select the GitHub repo**
5. **Set the Start Command:**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 10000
   ```
6. **Deploy & Get API URL**

---

## 🎯 **Contributing**
Feel free to submit PRs or raise issues!

---

## 📜 **License**
MIT License © 2025 Your Name
