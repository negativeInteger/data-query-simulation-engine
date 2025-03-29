from fastapi import Header, HTTPException
from app.models.schemas import CreatedUser
import jwt
from app.core.config import SECRET_KEY
from app.api.auth_routes import load_users
from typing import List




def verify_api_key(x_api_key: str = Header(None)):
    """Verify JWT API key from X-API-KEY header and extract user email."""
    if not x_api_key:
        raise HTTPException(status_code=400, detail="X-API-KEY header is missing")
    
    try:
        payload = jwt.decode(x_api_key, SECRET_KEY, algorithms=["HS256"])
        user_email = payload["email"] # Extract user email
        authenticated_users: List[CreatedUser] = load_users()
        for user in authenticated_users:
            if user.email == user_email and user.api_key == x_api_key:
                return
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="API key has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid API key")