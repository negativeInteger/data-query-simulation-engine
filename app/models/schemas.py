from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class QueryRequest(BaseModel):
    query: str = Field(..., example="Get all transactions where amount is greater than 300")

class QueryResponse(BaseModel):
    query: str = Field(..., example="Get all transactions where amount is greater than 300")
    data: Optional[List[Dict[str, Any]]] = Field(default=[], example=[{"id": 1, "amount": 500}])

class ExplainResponse(BaseModel):
    query: str = Field(..., example="Sort sales by region in ascending order")
    breakdown: Dict[str, Optional[str]] = Field(..., example={"operation": "sort", "field": "region", "order": "ascending"})

class ValidateResponse(BaseModel):
    query: str = Field(..., example="Get all customers")
    valid: bool = Field(..., example=False)

class User(BaseModel):
    email: str = Field(..., example="testuser@example.com")

class CreatedUser(BaseModel):
    email: str = Field(..., example="testuser@example.com")
    api_key: str = Field(..., example="123e4567-e89b-12d3-a456-426614174000")

class ApiKey(BaseModel):
    api_key: str = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
