from fastapi import FastAPI
from backend.app.routers.cards import router as card_router

app = FastAPI(title = "WIP---Website")

app.include_router(card_router)

@app.get("/")
def root():
    return {"message": "API Running!"}