from fastapi import APIRouter
from .service import get_all_states

router = APIRouter(prefix="/states", tags=["states"])

@router.get("/")
async def fetch_states():
    return await get_all_states()


    
