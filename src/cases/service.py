from app.models.requests import SearchRequest
from app.models.responses import CaseOut
from typing import List
from app.services.jagriti_client import JagritiClient
from app.services.case_parser import parse_cases_from_jagriti
from fastapi import HTTPException

async def search_cases_by_case_number(req: SearchRequest) -> List[CaseOut]:
    """Search cases by case number"""
    jc = JagritiClient()

    # 1. resolve state_id and commission_id
    state_id = await jc.resolve_state_id(req.state)
    if not state_id:
        raise HTTPException(status_code=400, detail="State not found")
    commission_id = await jc.resolve_commission_id(state_id, req.commission)
    if not commission_id:
        raise HTTPException(status_code=400, detail="Commission not found")

    # 2. call jagriti search endpoint
    raw = await jc.search_cases(
        search_type="CASE_NO",
        state_id=state_id,
        commission_id=commission_id,
        search_value=req.search_value,
        date_filter="filing_date",
        restrict_to="DAILY_ORDERS"
    )

    # 3. parse & format output
    cases = parse_cases_from_jagriti(raw)
    return cases

async def search_cases_by_complainant(req: SearchRequest) -> List[CaseOut]:
    """Search cases by complainant name"""
    jc = JagritiClient()

    # 1. resolve state_id and commission_id
    state_id = await jc.resolve_state_id(req.state)
    if not state_id:
        raise HTTPException(status_code=400, detail="State not found")
    commission_id = await jc.resolve_commission_id(state_id, req.commission)
    if not commission_id:
        raise HTTPException(status_code=400, detail="Commission not found")

    # 2. call jagriti search endpoint
    raw = await jc.search_cases(
        search_type="COMPLAINANT",
        state_id=state_id,
        commission_id=commission_id,
        search_value=req.search_value,
        date_filter="filing_date",
        restrict_to="DAILY_ORDERS"
    )

    # 3. parse & format output
    cases = parse_cases_from_jagriti(raw)
    return cases

async def search_cases_by_respondent(req: SearchRequest) -> List[CaseOut]:
    """Search cases by respondent name"""
    jc = JagritiClient()

    # 1. resolve state_id and commission_id
    state_id = await jc.resolve_state_id(req.state)
    if not state_id:
        raise HTTPException(status_code=400, detail="State not found")
    commission_id = await jc.resolve_commission_id(state_id, req.commission)
    if not commission_id:
        raise HTTPException(status_code=400, detail="Commission not found")

    # 2. call jagriti search endpoint
    raw = await jc.search_cases(
        search_type="RESPONDENT",
        state_id=state_id,
        commission_id=commission_id,
        search_value=req.search_value,
        date_filter="filing_date",
        restrict_to="DAILY_ORDERS"
    )

    # 3. parse & format output
    cases = parse_cases_from_jagriti(raw)
    return cases

async def search_cases_by_complainant_advocate(req: SearchRequest) -> List[CaseOut]:
    """Search cases by complainant advocate"""
    jc = JagritiClient()

    # 1. resolve state_id and commission_id
    state_id = await jc.resolve_state_id(req.state)
    if not state_id:
        raise HTTPException(status_code=400, detail="State not found")
    commission_id = await jc.resolve_commission_id(state_id, req.commission)
    if not commission_id:
        raise HTTPException(status_code=400, detail="Commission not found")

    # 2. call jagriti search endpoint
    raw = await jc.search_cases(
        search_type="COMPLAINANT_ADVOCATE",
        state_id=state_id,
        commission_id=commission_id,
        search_value=req.search_value,
        date_filter="filing_date",
        restrict_to="DAILY_ORDERS"
    )

    # 3. parse & format output
    cases = parse_cases_from_jagriti(raw)
    return cases

async def search_cases_by_respondent_advocate(req: SearchRequest) -> List[CaseOut]:
    """Search cases by respondent advocate"""
    jc = JagritiClient()

    # 1. resolve state_id and commission_id
    state_id = await jc.resolve_state_id(req.state)
    if not state_id:
        raise HTTPException(status_code=400, detail="State not found")
    commission_id = await jc.resolve_commission_id(state_id, req.commission)
    if not commission_id:
        raise HTTPException(status_code=400, detail="Commission not found")

    # 2. call jagriti search endpoint
    raw = await jc.search_cases(
        search_type="RESPONDENT_ADVOCATE",
        state_id=state_id,
        commission_id=commission_id,
        search_value=req.search_value,
        date_filter="filing_date",
        restrict_to="DAILY_ORDERS"
    )

    # 3. parse & format output
    cases = parse_cases_from_jagriti(raw)
    return cases

async def search_cases_by_industry_type(req: SearchRequest) -> List[CaseOut]:
    """Search cases by industry type"""
    jc = JagritiClient()

    # 1. resolve state_id and commission_id
    state_id = await jc.resolve_state_id(req.state)
    if not state_id:
        raise HTTPException(status_code=400, detail="State not found")
    commission_id = await jc.resolve_commission_id(state_id, req.commission)
    if not commission_id:
        raise HTTPException(status_code=400, detail="Commission not found")

    # 2. call jagriti search endpoint
    raw = await jc.search_cases(
        search_type="INDUSTRY_TYPE",
        state_id=state_id,
        commission_id=commission_id,
        search_value=req.search_value,
        date_filter="filing_date",
        restrict_to="DAILY_ORDERS"
    )

    # 3. parse & format output
    cases = parse_cases_from_jagriti(raw)
    return cases

async def search_cases_by_judge(req: SearchRequest) -> List[CaseOut]:
    """Search cases by judge name"""
    jc = JagritiClient()

    # 1. resolve state_id and commission_id
    state_id = await jc.resolve_state_id(req.state)
    if not state_id:
        raise HTTPException(status_code=400, detail="State not found")
    commission_id = await jc.resolve_commission_id(state_id, req.commission)
    if not commission_id:
        raise HTTPException(status_code=400, detail="Commission not found")

    # 2. call jagriti search endpoint
    raw = await jc.search_cases(
        search_type="JUDGE",
        state_id=state_id,
        commission_id=commission_id,
        search_value=req.search_value,
        date_filter="filing_date",
        restrict_to="DAILY_ORDERS"
    )

    # 3. parse & format output
    cases = parse_cases_from_jagriti(raw)
    return cases
