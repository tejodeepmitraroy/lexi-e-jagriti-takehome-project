from fastapi import APIRouter
from src.core.model import ApiResponse
from .controller import get_all_states

router = APIRouter(prefix="/states", tags=["states"])

@router.get("/", response_model=ApiResponse)
async def fetch_states():
    return await get_all_states()


    
