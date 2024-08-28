from fastapi.routing import APIRouter
from server.fastapi.routes.example import router as example_router

router = APIRouter()

router.include_router(example_router)
