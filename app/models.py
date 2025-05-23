
from pydantic import BaseModel

class IncomingMessage(BaseModel):
    body: str
    sender: str

class RoutedMessage(BaseModel):
    intent: str
    entities: list[str]
    action: str  # "route" or "log"
    recipient: str | None = None
