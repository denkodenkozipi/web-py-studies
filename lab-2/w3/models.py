from pydantic import BaseModel, model_validator

class User(BaseModel):
    name: str
    age: int
    is_adult: bool = False

    @model_validator(mode="after")
    def set_adult_status(self) -> 'User':
        self.is_adult = self.age >= 18
        return self

class FeedBack(BaseModel):
    name: str
    message: str
