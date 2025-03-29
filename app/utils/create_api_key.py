from datetime import datetime, timezone, timedelta
from app.core.config import SECRET_KEY
from app.models.schemas import User
import jwt

utc_now = datetime.now(timezone.utc)

def create_api_key(user: User):
    """Generate a JWT-based API-Key using the user's email."""
    
    payload = {
        "email": user.email,  # Store user's email in the token
        "exp": datetime.utcnow() + timedelta(days=30)
    }

    # Generate JWT token
    token = jwt.encode(payload, SECRET_KEY , algorithm="HS256")
    return token
