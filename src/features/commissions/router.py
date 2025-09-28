from fastapi import APIRouter
from src.core.model import ApiResponse
from .controller import list_commissions

router = APIRouter(prefix="/commissions", tags=["commissions"])

@router.get("/")
async def fetch_commissions_list():
    return {}

@router.get("/{commission_id}",response_model=ApiResponse)
async def get_commissions_list_by_id(commission_id: int):
    return await list_commissions(commission_id)
    