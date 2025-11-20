from pydantic import BaseModel

class CodeSnippet(BaseModel):
    id: int
    code: str
    description: str