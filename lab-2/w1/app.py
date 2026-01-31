from models import User
from fastapi import FastAPI

app = FastAPI()

users = [
    User(name="John Doe", id = 1,),
    User(name="Barbara Dey", id = 2,),
    User(name="Leni Bibi", id = 3,),
    User(name="Tzar Ivan", id = 4,),
]
@app.get("/users")
def read_root():
    return {"users": users}
