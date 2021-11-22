from typing import Optional, List
from pydantic import BaseModel, validator

from survey.question import BaseQuestion


class Survey(BaseModel):
    id : Optional[str]
    title : str
    data : List[BaseQuestion]

    @validator("data")
    def validate_data(cls, var) :
        if not isinstance(var,BaseQuestion):
            raise TypeError("Invalid Type")
        return var
        