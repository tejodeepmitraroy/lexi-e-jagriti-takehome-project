from fastapi import APIRouter, HTTPException
from app.models.requests import SearchRequest
from app.models.responses import CaseOut
from typing import List
from app.services.jagriti_client import JagritiClient
from app.services.case_parser import parse_cases_from_jagriti

router = APIRouter()
jc = JagritiClient()

@router.post("/by-case-number", response_model=List[CaseOut])
async def search_by_case_number(req: SearchRequest):
    # 1. resolve state_id and commission_id
    state_id = await jc.resolve_state_id(req.state)
    if not state_id:
        raise HTTPException(status_code=400, detail="State not found")
    commission_id = await jc.resolve_commission_id(state_id, req.commission)
    if not commission_id:
        raise HTTPException(status_code=400, detail="Commission not found")
    # 2. call jagriti search endpoint
    raw = await jc.search_cases(
        search_type="CASE_NO",   # hypothetical param matching Jagriti
        state_id=state_id,
        commission_id=commission_id,
        search_value=req.search_value,
        date_filter="filing_date",
        restrict_to="DAILY_ORDERS"  # enforce Daily Orders only
    )
    # 3. parse & format output
    cases = parse_cases_from_jagriti(raw)
    return cases