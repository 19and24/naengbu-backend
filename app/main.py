from fastapi import FastAPI

from app.models import Ingredient

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Fridge"}