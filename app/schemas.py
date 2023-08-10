from pydantic import BaseModel
from enum import Enum 

class RoleEnum(str, Enum):
    system = "system"
    assistant = "assistant"
    user = "user"

class ExistingContext(BaseModel):
    role: RoleEnum
    content: str

    class Config: 
        use_enum_values = True

class ChatRequest(BaseModel):
    existing_context: ExistingContext | None = None
    query: str

class ChatResponse(BaseModel):
    response: str