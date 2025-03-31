from fastapi import APIRouter, Depends, HTTPException
from app.services.query_processor import process_query, explain_query, validate_query
from app.utils.verify_api_key import verify_api_key
from app.models.schemas import QueryRequest, QueryResponse, ExplainResponse, ValidateResponse

# Router for handling query-related endpoints
query_router = APIRouter()

@query_router.post("/api/query", response_model=QueryResponse, dependencies=[Depends(verify_api_key)], tags=['Query'])
def query_endpoint(request: QueryRequest):
    """
    Convert a natural language query into an SQL query and return the simulated response data.
    """
    sql_query, data = process_query(request.query)
    return {"query": sql_query, "data": data}

@query_router.post("/api/explain", response_model=ExplainResponse, dependencies=[Depends(verify_api_key)], tags=['Explain'])
def explain_endpoint(request: QueryRequest):
    """
    Explain the processing steps involved in handling the given query.
    """
    breakdown = explain_query(request.query)
    return {"query": request.query, "breakdown": breakdown}

@query_router.post("/api/validate", response_model=ValidateResponse, dependencies=[Depends(verify_api_key)], tags=['Validate'])
def validate_endpoint(request: QueryRequest):
    """
    Validate whether the given query is structured correctly and feasible.
    """
    valid = validate_query(request.query)
    return {"query": request.query, "valid": valid}
