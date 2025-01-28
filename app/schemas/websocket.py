""" Websocket messages schema  """
from pydantic import BaseModel
from typing import Optional


class MessageSchema(BaseModel):
    """ Messahe Schema """
    content: str
    notify_all: Optional[bool] = None
    recipient: Optional[str] = None

