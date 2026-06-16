import uvicorn
from fastapi import FastAPI
from api import router as api_router

app = FastAPI(title="MEGA TITLE TEXT")
app.include_router(api_router)


def start_server():
    """ Start the server"""
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    start_server()
