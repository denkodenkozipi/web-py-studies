from models import User, FeedBack
from fastapi import FastAPI

app = FastAPI()

users = [
    User(name="Ada Lovelace", age=12),
    User(name="Linus Torvalds", age=53),
    User(name="Grace Hopper", age=119),
    User(name="Guido van Rossum", age=11),
]


feedbacks = [
    FeedBack(name="Ada Lovelace", message="Your site runs smoother than my analytical engine on a good day!"),
    FeedBack(name="Linus Torvalds", message="Why does the UI feel like a kernel panic? Debug it, please!"),
    FeedBack(name="Grace Hopper", message="Excellent! It’s as user‑friendly as a COBOL compiler with good documentation."),
    FeedBack(name="Guido van Rossum", message="Indentation is fine, but the layout could use a bit more Pythonic elegance."),
]


@app.get("/users")
def get_all_users():
    return {
        "total": len(users),
        "users": users,
    }


@app.post("/user")
async def create_user(user: User):
    users.append(user)
    return {
        "message": "user created successfully!",
        "user": user,
    }


@app.get("/feedbacks")
def get_all_feedbacks():
    return {
        "total": len(feedbacks),
        "feedbacks": feedbacks,
    }

@app.post("/feedback")
async def submit_feedback(feedback: FeedBack):
    feedbacks.append(feedback)
    return {
        "message": f"Thank you, {feedback.name}! Your feedback has been saved."
    }