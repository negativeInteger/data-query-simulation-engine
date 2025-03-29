import json
import os
from fastapi import HTTPException, APIRouter
from app.models.schemas import User, CreatedUser, ApiKey
from app.utils.create_api_key import create_api_key
from typing import List

DATA_FILE = "users.json"

# Load existing users from file
def load_users() -> List[CreatedUser]:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
                return [CreatedUser(**user) for user in data]  # Convert dict to CreatedUser objects
            except json.JSONDecodeError:
                return []
    return []

# Save users to file
def save_users():
    with open(DATA_FILE, "w") as f:
        json.dump([user.model_dump() for user in authenticated_users], f, indent=4)

# Initialize the users list from file
authenticated_users: List[CreatedUser] = load_users()

auth_router = APIRouter()

@auth_router.post("/api/auth/signup", response_model=CreatedUser, status_code=201, tags=['SignUp'])
def signup(new_user: User):
    if not new_user.email:
        raise HTTPException(status_code=400, detail="Email is required")
    
    global authenticated_users
    for user in authenticated_users:
        if user.email == new_user.email:
            raise HTTPException(status_code=409, detail="API-KEY already exists for this email")

    # Create API key and add user
    api_key = create_api_key(new_user)
    createdUser = CreatedUser(email=new_user.email, api_key=api_key)

    authenticated_users.append(createdUser)
    save_users()  # Persist to JSON file

    return createdUser
