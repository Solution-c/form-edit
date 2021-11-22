from typing import Optional


class BaseQuestion:
    def __init__(
        self, title: str, answer: Optional[str] = None, required: bool = False
    ):
        self.title = title
        self.answer = answer
        self.required = required


class TextQuestion(BaseQuestion):
    pass


class OptionalQuestion(BaseQuestion):
    def __init__(
        self,
        title: str,
        options: list,
        answer: Optional[str] = None,
        required: bool = False,
    ):
        super().__init__(title, answer, required)
        self.options = options


class FileQuesiton(BaseQuestion):
    pass
