from fastapi import Depends, HTTPException, Header
import os

def api_key_auth(x_api_key: str = Header(...)):
    """Lightweight API Key Authentication."""
    if x_api_key != os.getenv("API_KEY"):
        raise HTTPException(status_code=403, detail="Invalid API Key.")
