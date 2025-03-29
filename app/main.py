from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from app.api.query_routes import query_router
from app.api.auth_routes import auth_router

app = FastAPI(
    title="Data Query Simulation Engine",
    description=(
        "A FastAPI-based service that converts natural language queries into pseudo-SQL. "
        "It provides explanations, validates query feasibility, and ensures secure API access with API key authentication."
    ),
    version="1.0.0",
)

# Include API routes
app.include_router(auth_router)
app.include_router(query_router)

# Root Endpoint
@app.get("/", response_class=HTMLResponse, tags=['Root'])
def read_root(request: Request):

    base_url = str(request.base_url).rstrip("/")  # Removes trailing "/"
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
                background-color: #f4f4f4;
            }}
            h1 {{
                color: #333;
            }}
            p {{
                color: #666;
            }}
            a {{
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                text-decoration: none;
                color: white;
                background-color: #007bff;
                border-radius: 5px;
            }}
            a:hover {{
                background-color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <h1>Welcome to the Data Query Simulation Engine</h1>
        <p>Explore the API and run your queries with ease!</p>
        <a href="{base_url}/docs">Swagger Docs</a>
    </body>
    </html>
    """