from dataclasses import dataclass
from typing import Optional, List, Union

from pydantic import BaseModel, validator


class BaseQuestion:
    def __init__(
        self, title: str, required: bool = False, answer: Optional[str] = None
    ):
        self.title = title
        self.required = required
        self.answer = answer

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, var: dict):
        if not isinstance(var, dict):
            raise TypeError("Request body is not JSON")

        instance = cls(**var)
        for key, value in var.items():
            if not isinstance(value, type(getattr(instance, key))):
                raise TypeError(f"Invalid Type: expected {type(value)}")
        return instance


class TextQuestion(BaseQuestion):
    pass


class OptionalQuestion(BaseQuestion):
    def __init__(
        self,
        title: str,
        options: list,
        required=False,
        answer: Optional[str] = None,
    ):
        super().__init__(title, required, answer)
        self.options = options


class FileQuesiton(BaseQuestion):
    pass


class Survey(BaseModel):
    id: Optional[str]
    title: str
    data: List[
        Union[BaseQuestion, TextQuestion, OptionalQuestion, FileQuesiton]
    ]
