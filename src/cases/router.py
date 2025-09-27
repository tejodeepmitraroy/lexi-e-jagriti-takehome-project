from fastapi import APIRouter

from .schemas import CaseByCaseNumberRequest, CaseByComplainantRequest, CaseByRespondentRequest, CaseByComplainantAdvocateRequest, CaseByRespondentAdvocateRequest, CaseByIndustryTypeRequest, CaseByJudgeRequest
from .service import search_cases_by_case_number, search_cases_by_complainant, search_cases_by_respondent, search_cases_by_complainant_advocate, search_cases_by_respondent_advocate, search_cases_by_industry_type, search_cases_by_judge


router = APIRouter(prefix="/cases", tags=["cases"])

@router.post("/by-case-number")
async def fetch_cases_list(body:CaseByCaseNumberRequest):
    return await search_cases_by_case_number(body)
    
@router.post("/by-complainant")
async def fetch_cases_list(body:CaseByComplainantRequest):
    return await search_cases_by_complainant(body)

@router.post("/by-respondent")
async def fetch_cases_list(body:CaseByRespondentRequest ):
    return await search_cases_by_respondent(body)

@router.post("/by-complainant-advocate")
async def fetch_cases_list(body:CaseByComplainantAdvocateRequest):
    return await search_cases_by_complainant_advocate(body)

@router.post("/by-respondent-advocate")
async def fetch_cases_list(body:CaseByRespondentAdvocateRequest):
    return await search_cases_by_respondent_advocate(body)   

@router.post("/by-industry-type")
async def fetch_cases_list(body:CaseByIndustryTypeRequest):
    return await search_cases_by_industry_type(body)

@router.post("/by-judge")
async def fetch_cases_list(body:CaseByJudgeRequest):
    return await search_cases_by_judge(body)

