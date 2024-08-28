from fastapi import FastAPI
import uvicorn
from server.fastapi.routes.router import router

class CreateFastAPIServer:
    def __init__(self):
        self.app = FastAPI()
        self.app.include_router(router)

    def run(self):
        uvicorn.run(self.app, host="0.0.0.0", port=8000)
