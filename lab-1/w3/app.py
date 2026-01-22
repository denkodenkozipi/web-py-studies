from fastapi import FastAPI

app = FastAPI()

@app.get("/calculate")
def add(num1: float, num2:float):
    return {
        "num1": num1,
        "num2": num2,
        "sum": num1 + num2,
    }