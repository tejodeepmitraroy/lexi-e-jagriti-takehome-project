from pydantic import BaseModel

class CaseResponse(BaseModel):
    case_number: str
    case_stage: str
    filing_date: str   # ISO date
    complainant: str
    complainant_advocate: str | None
    respondent: str
    respondent_advocate: str | None
    document_link: str | None


class CaseRequest(BaseModel):
    case_number: str