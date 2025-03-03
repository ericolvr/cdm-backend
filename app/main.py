""" App entrypoint """
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints.apartment import apartment_routes
from app.api.v1.endpoints.complex import complex_routes
from app.api.v1.endpoints.people import people_routes
from app.api.v1.endpoints.user import user_routes
from app.api.v1.endpoints.vehicle import vehicle_routes
from app.api.v1.endpoints.token import token_routes
from app.api.v1.endpoints.place import place_routes
from app.api.v1.endpoints.websocket import message_routes


app = FastAPI()

origins = [
    'http://localhost',
    'http://localhost:5173',
    'http://127.0.0.1:5173',
    'http://127.0.0.1',    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(apartment_routes)
app.include_router(complex_routes)
app.include_router(people_routes)
app.include_router(user_routes)
app.include_router(vehicle_routes)
app.include_router(token_routes)
app.include_router(place_routes)
app.include_router(message_routes)


