from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

# Request model for processing a natural language query
class QueryRequest(BaseModel):
    query: str = Field(..., example="Get all transactions where amount is greater than 300")

# Response model for processed queries, returning SQL and optional result data
class QueryResponse(BaseModel):
    query: str = Field(..., example="SELECT * FROM transactions WHERE amount > 300;")
    data: Optional[List[Dict[str, Any]]] = Field(example=[
        {
            "id": 102,
            "amount": 500,
            "status": "pending"
        }
    ])

# Response model for explaining how a query is interpreted
class ExplainResponse(BaseModel):
    query: str = Field(..., example="Get all transactions where amount is greater than 300")
    breakdown: Dict[str, Optional[str]] = Field(..., example={
        "action": "fetch",
        "table": "transactions",
        "filter": "amount greater than 300",
        "sort": None,
        "aggregation": None
    })

# Response model for validating a query’s correctness
class ValidateResponse(BaseModel):
    query: str = Field(..., example="Get all transactions where amount is greater than 300")
    valid: bool = Field(..., example=True)

# Request model for user signup
class User(BaseModel):
    email: str = Field(..., example="testuser@example.com")

# Response model for a successfully created user with an API key
class CreatedUser(BaseModel):
    email: str = Field(..., example="testuser@example.com")
    api_key: str = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
