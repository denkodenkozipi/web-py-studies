from models import User
from fastapi import FastAPI

app = FastAPI()

users = [
    User(name="John Doe", age=19),
    User(name="Barbara Dey", age=22),
    User(name="Leni Bibi", age=32),
    User(name="Tzar Ivan", age=197),
]
@app.get("/users")
def read_root():
    return {"users": users}

@app.post("/user/")
async def create_user(user: User):
    return {"message": "successfully!", "user": user}