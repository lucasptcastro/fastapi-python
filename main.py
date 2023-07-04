# Libs: fastapi, uvicorn
# To execute: uvicorn "arquivo":app --reload

from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa", "preco_unitario": 34, "quantidade": 7},
    3: {"item": "copo", "preco_unitario": 76, "quantidade": 1},
    4: {"item": "prato", "preco_unitario": 21, "quantidade": 3},
}


@app.get("/")
def home():
    return {"Vendas": len(vendas)}


@app.get("/vendas/{id}")
def pegar_venda(id: int):
    return vendas[id]
