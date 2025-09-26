from fastapi import APIRouter
from .cases import list_cases

router = APIRouter(prefix="/cases", tags=["cases"])

@router.get("/by-case-number")
async def fetch_cases_list():
    return {}
    
@router.get("/by-complainant")
async def fetch_cases_list():
    return {}

@router.get("/by-respondent")
async def fetch_cases_list():
    return {}

