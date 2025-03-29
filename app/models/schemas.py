from pydantic import BaseModel
from typing import List, Dict, Any

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    query: str
    data: List[Dict[str, Any]]

class ExplainResponse(BaseModel):
    query: str
    breakdown: Dict[str, str]

class ValidateResponse(BaseModel):
    query: str
    valid: bool
