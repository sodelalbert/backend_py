from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def read_root() -> dict:
    return {"message": "Hello World"}


@app.get("/greet/{name}")
async def greet(name: str) -> dict:
    return {"message": f"Hello, {name}"}
