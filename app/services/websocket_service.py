""" Websocket connection manager """
from typing import Dict
from fastapi import WebSocket


class Manager:
    """ Connection Manager """

    def __init__(self) -> None:
        self.active_connections: Dict[str, WebSocket] = {}


    async def connect(self, websocket: WebSocket, user: str):
        """ Connect """

        await websocket.accept()
        self.active_connections[user] = websocket


    async def disconnect(self, user: str):
        """ Disconnect """

        if user in self.active_connections:
            del self.active_connections[user]

    
    async def send_personal(self, message: str, user: str):
        """ Send personal message method """

        if user in self.active_connections:
            await self.active_connections[user].send_text(message)


    async def broadcast(self, message: str):
        """ Broadcast Messages """

        for conn in self.active_connections.values():
            await conn.send_json(message)


manager = Manager()


