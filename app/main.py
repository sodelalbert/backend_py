from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
async def read_root() -> dict:
    return {"message": "Hello World"}


# Mix path parameters and query parameters
@app.get("/greet/{name}")
async def greet(name: str, age: int) -> dict:
    return {"message": f"Hello, {name}, age {age}"}


# Optional query parameters


@app.get("/greet")
async def greet_user(age: int = 0, name: Optional[str] = "User") -> dict:
    return {"message": f"Hello, {name}", "age": f"{age}"}


class UserCreateModel(BaseModel):
    name: str
    age: int


@app.post("/create_user")
async def create_user(user_data: UserCreateModel) -> dict:
    return {
        "name": f"{user_data.name}",
        "age": f"{user_data.age}",
    }


@app.get("/get_headers", status_code=211)
async def get_headers(
    accept: str = Header(None), content_type: str = Header(None)
) -> dict:
    request_headers = {}

    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type

    return request_headers
