""" Websocket routes """
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.schemas.websocket import MessageSchema
from app.services.websocket_service import manager


message_routes = APIRouter(
    prefix='/api/v1/ws',
    tags=['Messages']
)


@message_routes.websocket('/{user}')
async def websocket(websocket: WebSocket, user: str):
    """ Websocket connections """

    try:
        await manager.connect(websocket, user)
        await manager.send_personal(f'Bem-vindo usuário: {user}', user)

        while True:
            data = await websocket.receive_json()
            message = MessageSchema.model_validate(data)
            
            await test_messages(message)

            if message.notify_all:
                await manager.broadcast(f'Mensagem para todos: {message.content}')
            else:
                await manager.send_personal(
                    f'Mensagem pessoal: {message.content}',
                    message.recipient
                )

    except WebSocketDisconnect:
        await manager.disconnect(user)
        await manager.broadcast(f'User {user} disconnected from server')


async def test_messages(message: MessageSchema):
    """ Test message """
    print(message, '-------------->')
    return message