from pydantic import BaseModel


class InputUserMessage(BaseModel):
    message: str