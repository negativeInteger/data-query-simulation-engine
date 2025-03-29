from fastapi import APIRouter, Depends, HTTPException
from app.services.query_processor import process_query, explain_query, validate_query
from app.utils.verify_api_key import verify_api_key
from app.models.schemas import QueryRequest, QueryResponse, ExplainResponse, ValidateResponse

query_router = APIRouter()


@query_router.post("/api/query", response_model=QueryResponse, dependencies=[Depends(verify_api_key)], tags=['Query'])
def query_endpoint(request: QueryRequest):
    """Process a natural language query and return a simulated SQL response."""
    sql_query, data = process_query(request.query)
    return {"query": sql_query, "data": data}

@query_router.post("/api/explain", response_model=ExplainResponse, dependencies=[Depends(verify_api_key)], tags=['Explain'])
def explain_endpoint(request: QueryRequest):
    """Explain how the query is being processed."""
    breakdown = explain_query(request.query)
    return {"query": request.query, "breakdown": breakdown}

@query_router.post("/api/validate", response_model=ValidateResponse, dependencies=[Depends(verify_api_key)], tags=['Validate'])
def validate_endpoint(request: QueryRequest):
    """Validate a query's feasibility."""
    valid = validate_query(request.query)
    if not valid:
        raise HTTPException(status_code=400, detail="Invalid query structure.")
    return {"query": request.query, "valid": True}
