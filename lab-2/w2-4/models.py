from pydantic import BaseModel, model_validator, field_validator
from typing import ClassVar
import re


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

    FORBIDDEN_WORDS: ClassVar[list[str]] =\
        [
        "редиска",
        "бяка",
        "козявка",
        ]

    MAX_LEN_NAME: ClassVar[int] = 50
    MIN_LEN_NAME: ClassVar[int] = 2

    MAX_LEN_MESSAGE: ClassVar[int] = 500
    MIN_LEN_MESSAGE: ClassVar[int] = 2

    @field_validator("name")
    def name_validator_len(cls, v):
        if len(v) > cls.MAX_LEN_NAME:
            raise ValueError(f"Name cannot exceed {cls.MAX_LEN_NAME} characters")
        elif len(v) < cls.MIN_LEN_NAME:
            raise ValueError(f"Name must be at least {cls.MIN_LEN_NAME} character")
        return v

    @field_validator("message")
    def message_validator_len(cls, v):
        if len(v) > cls.MAX_LEN_MESSAGE:
            raise ValueError(f"Review is too long - maximum {cls.MAX_LEN_MESSAGE} characters.")
        elif len(v) < cls.MIN_LEN_MESSAGE:
            raise ValueError(f"Review is too short - minimum {cls.MIN_LEN_MESSAGE} characters")


        pattern = cls._build_forbidden_pattern()

        if pattern.search(v):
            raise ValueError("Disallowed words used")

        return v

    @classmethod
    def _build_forbidden_pattern(cls) -> re.Pattern:
        stems = [re.escape(word[:-1]) for word in cls.FORBIDDEN_WORDS]
        regex = rf"\b({'|'.join(stems)})\w*\b"
        return re.compile(regex, re.IGNORECASE)