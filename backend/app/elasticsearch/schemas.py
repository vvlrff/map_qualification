from pydantic import BaseModel


class InputUserMessage(BaseModel):
    message: str


class InputUserMessageDate(BaseModel):
    message: str
    begin: str
    end: str