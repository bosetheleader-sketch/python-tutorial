# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Simple REST API")


class User(BaseModel):
    name: str
    email: str


users = {
    1: {
        "name": "Mohan",
        "email": "mohan@example.com"
    }
}


@app.get("/")
def home():
    return {"message": "REST API is running"}


@app.get("/users")
def get_users():
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = users.get(user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@app.post("/users", status_code=201)
def create_user(user: User):
    user_id = max(users.keys(), default=0) + 1

    users[user_id] = user.model_dump()

    return {
        "message": "User created successfully",
        "user_id": user_id,
        "user": users[user_id]
    }


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    users[user_id] = user.model_dump()

    return {
        "message": "User updated successfully",
        "user": users[user_id]
    }


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    deleted_user = users.pop(user_id)

    return {
        "message": "User deleted successfully",
        "user": deleted_user
    }
