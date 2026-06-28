from fastapi import FastAPI
from routes.chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(chat_router)

@app.get("/")
def root():
    return {"status": "AI Research Assistant running"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)