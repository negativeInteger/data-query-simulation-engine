from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class QueryRequest(BaseModel):
    query: str = Field(..., example="Get all transactions where amount is greater than 300")

class QueryResponse(BaseModel):
    query: str = Field(..., example="SELECT * FROM transactions WHERE amount > 300;")
    data: Optional[List[Dict[str, Any]]] = Field(example=[
        {
            "id": 102,
            "amount": 500,
            "status": "pending"
        }
    ])

class ExplainResponse(BaseModel):
    query: str = Field(..., example="Get all transactions where amount is greater than 300")
    breakdown: Dict[str, Optional[str]] = Field(..., example={
        "action": "fetch",
        "table": "transactions",
        "filter": "amount greater than 300",
        "sort": None,
        "aggregation": None
    })

class ValidateResponse(BaseModel):
    query: str = Field(..., example="Get all transactions where amount is greater than 300")
    valid: bool = Field(..., example=True)

class User(BaseModel):
    email: str = Field(..., example="testuser@example.com")

class CreatedUser(BaseModel):
    email: str = Field(..., example="testuser@example.com")
    api_key: str = Field(..., example="123e4567-e89b-12d3-a456-426614174000")

class ApiKey(BaseModel):
    api_key: str = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
