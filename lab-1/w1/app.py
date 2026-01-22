from fastapi import FastAPI
from datetime import datetime

today = datetime.now().date().isoformat()
app = FastAPI()

@app.get("/")
def read_root():
    return {
        "Date": today,
        "Hello!": "World",
    }