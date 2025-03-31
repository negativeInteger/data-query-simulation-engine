from fastapi import Header, HTTPException
from app.models.schemas import CreatedUser
import jwt
from app.core.config import SECRET_KEY
from app.api.auth_routes import load_users
from typing import List




def verify_api_key(x_api_key: str = Header(None)):
    """
    Verify JWT API Key from X-API-KEY header and extract user email.

    This function checks if a valid API key (JWT token) is provided in the 
    X-API-KEY header. It decodes the token to retrieve the user's email and 
    verifies if the corresponding user exists in the list of authenticated users.

    Args:
        x_api_key (str): API key passed in the X-API-KEY header.
    
    Raises:
        HTTPException: 
            - If the X-API-KEY header is missing (400).
            - If the API key is expired (401).
            - If the API key is invalid (401).
            - If no matching user is found (401).
    """
    if not x_api_key:
        raise HTTPException(status_code=400, detail="X-API-KEY header is missing")
    
    try:
        payload = jwt.decode(x_api_key, SECRET_KEY, algorithms=["HS256"])
        user_email = payload["email"] # Extract user email
        # Load authenticated users from the mock database
        authenticated_users: List[CreatedUser] = load_users()
        for user in authenticated_users:
            if user.email == user_email and user.api_key == x_api_key:
                return  # If a matching user and API key are found, continue without error
    except jwt.ExpiredSignatureError:
        # JWT Token Expiration Error
        raise HTTPException(status_code=401, detail="API key has expired")
    except jwt.InvalidTokenError:
        # Invalid Token Error
        raise HTTPException(status_code=401, detail="Invalid API key")