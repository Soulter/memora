from pydantic import BaseModel

class Response(BaseModel):
    status: str
    message: str
    data: dict | None = None
