from fastapi import APIRouter
from .service import list_commissions

router = APIRouter(prefix="/commissions", tags=["commissions"])

@router.get("/")
async def fetch_commissions_list():
    return {}

@router.get("/{commission_id}")
async def get_commissions_list_by_id(commission_id: int):
    return await list_commissions(commission_id)
    