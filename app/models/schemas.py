from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    query: str
    data: Optional[List[Dict[str, Any]]] = []

class ExplainResponse(BaseModel):
    query: str
    breakdown: Dict[str, Optional[str]]

class ValidateResponse(BaseModel):
    query: str
    valid: bool

class User(BaseModel):
    email: str

class CreatedUser(BaseModel):
    email: str
    api_key: str

class ApiKey(BaseModel):
    api_key: str
