from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import (accounts,
                     movies,
                     showtimes,
                     seats,
                     rooms,
                     bookings,
                     upcomingMovie)
from authenticator import authenticator
import os

app = FastAPI()
app.include_router(accounts.router)
app.include_router(authenticator.router)
app.include_router(movies.router)
app.include_router(seats.router)
app.include_router(rooms.router)
app.include_router(upcomingMovie.router)

app.include_router(showtimes.router)
app.include_router(bookings.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_HOST", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
