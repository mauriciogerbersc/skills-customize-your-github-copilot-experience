from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API FastAPI!"}

@app.post("/data")
def create_item(item: Item):
    return {"message": f"Olá, {item.name}! Sua solicitação foi recebida."}