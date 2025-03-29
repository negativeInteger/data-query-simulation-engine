mock_data = {
    "sales": [
        {"id": 1, "region": "North", "revenue": 5000},
        {"id": 2, "region": "South", "revenue": 3000}
    ],
    "transactions": [
        {"id": 101, "amount": 250, "status": "completed"},
        {"id": 102, "amount": 500, "status": "pending"}
    ]
}

def process_query(natural_query: str):
    """Convert a natural language query into pseudo-SQL and return mock data."""
    if "sales" in natural_query.lower():
        return "SELECT * FROM sales;", mock_data["sales"]
    elif "transactions" in natural_query.lower():
        return "SELECT * FROM transactions;", mock_data["transactions"]
    else:
        return "INVALID_QUERY", []
    
def explain_query(natural_query: str):
    """Break down a query into components."""
    return {"action": "fetch", "table": "sales" if "sales" in natural_query else "transactions"}

def validate_query(natural_query: str) -> bool:
    """Check if the query is about supported datasets."""
    return any(keyword in natural_query.lower() for keyword in ["sales", "transactions"])

