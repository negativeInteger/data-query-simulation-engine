from datetime import datetime, timezone, timedelta
from app.core.config import SECRET_KEY
from app.models.schemas import User
import jwt

utc_now = datetime.now(timezone.utc)

def create_api_key(user: User):
    """
    Generates a secure JWT-based API key using the user's email.

    The API key (JWT token) contains:
    - `email`: Identifies the user
    - `exp`: Expiration timestamp (30 days from now)
    
    Args:
        user (User): The user object containing email.

    Returns:
        str: A signed JWT token as the API key.
    """
    
    payload = {
        "email": user.email,  # Store user's email in the token
        "exp": datetime.now(timezone.utc) + timedelta(days=30)  # Expiration in UTC
    }


    # Generate JWT token with HS256 algorithm
    token = jwt.encode(payload, SECRET_KEY , algorithm="HS256")
    return token
