from fastapi import FastAPI, HTTPException

from .schemas import *
from .helpers import *

def create_app():
    app = FastAPI()

    @app.get("/", tags=["Healthcheck"])
    async def root():
        return {"message": "I'm Alive"}


    @app.post("/chat", tags=["Chat API"], response_model=ChatResponse)
    async def chat(query: ChatRequest):
        existing_context = query.existing_context or []
        query = query.query
        print("QUERY RECEIVED")
        try:
            return {"response": chat_gpt_query(query) }
        except Exception as e:
            return HTTPException(status_code=500, detail=str(e))
        

    return app

