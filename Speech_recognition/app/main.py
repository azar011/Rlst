from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all frontend origins
    # allow_origins=[
    #     "http://localhost:5500",
    #     "https://yourdomain.com"
    # ]    #For Production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Whisper Translation API Running"
    }

    
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
