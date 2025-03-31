import json
import os
from fastapi import HTTPException, APIRouter
from app.models.schemas import User, CreatedUser
from app.utils.create_api_key import create_api_key
from typing import List

# Mock Database file
DATA_FILE = "users.json"

def load_users() -> List[CreatedUser]:
    """
    Load existing users from the JSON file.
    Returns a list of CreatedUser objects.
    """
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
                return [CreatedUser(**user) for user in data]  # Convert dict to CreatedUser objects
            except json.JSONDecodeError:
                return [] # Return empty list if JSON is corrupted
    return [] # Return empty list if file doesn't exist

def save_users():
    """
    Save the current authenticated users list to the JSON file.
    """
    with open(DATA_FILE, "w") as f:
        json.dump([user.model_dump() for user in authenticated_users], f, indent=4)

# Initialize the users list from JSON file
authenticated_users: List[CreatedUser] = load_users()

# Router for handling auth-related endpoint
auth_router = APIRouter()

@auth_router.post("/api/auth/signup", response_model=CreatedUser, status_code=201, tags=['SignUp'])
def signup(new_user: User):
    """
    Register a new user by generating an API key.
    - Returns a CreatedUser object containing the email and API key.
    - If the email already exists, returns a 409 Conflict error.
    """
    if not new_user.email:
        raise HTTPException(status_code=400, detail="Email is required")
    
    global authenticated_users
    for user in authenticated_users:
        if user.email == new_user.email:
            raise HTTPException(status_code=409, detail="API-KEY already exists for this email")

    # Generate API key for the new user
    api_key = create_api_key(new_user)
    created_user = CreatedUser(email=new_user.email, api_key=api_key)

    # Store user and persist changes
    authenticated_users.append(created_user)
    save_users()  

    return created_user
