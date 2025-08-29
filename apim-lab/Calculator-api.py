from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Calculator API", version="1.0")

class Operands(BaseModel):
    a: float
    b: float

@app.get("/")
def home():
    return {"message": "Calculator API - use /docs or /openapi.json"}

# GET endpoints (query params)
@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/sub")
def sub(a: float, b: float):
    return {"result": a - b}

@app.get("/mul")
def mul(a: float, b: float):
    return {"result": a * b}

@app.get("/div")
def div(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero")
    return {"result": a / b}

