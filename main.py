from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from chat import router


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("🚀 TAYF AI Server started successfully")
    print("☀️ Solar Intelligence Assistant is ready")

    yield

    print("🛑 TAYF AI Server stopped")


app = FastAPI(
    title="TAYF Solar AI Assistant API",
    description=(
        "AI-powered conversational assistant for "
        "TAYF Solar Plant Intelligence Platform."
    ),
    version="1.0.0",
    lifespan=lifespan
)


app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "message": "TAYF Solar AI Assistant API is running ☀️",
        "status": "active",
        "project": "TAYF",
        "endpoints": {
            "chat": "/api/chat",
            "health": "/health",
            "docs": "/docs"
        }
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "TAYF Solar AI Assistant"
    }


# IMPORTANT:
# router already contains /api
app.include_router(router)