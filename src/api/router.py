from fastapi import APIRouter
from src.states.router import router as states_router
from src.comissions.router import router as commissions_router

api_router = APIRouter()
api_router.include_router(states_router)
api_router.include_router(commissions_router)