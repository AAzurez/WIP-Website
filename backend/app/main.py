from fastapi import FastAPI

app = FastAPI(title = "WIP---Website")

@app.get("/")
def root():
    return {"message": "Hello, World!"}