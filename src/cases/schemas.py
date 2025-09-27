from typing import List, Optional, Union
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


class CaseDetailsBySearchRequest(BaseModel):
    commissionId:int
    dateRequestType:int
    fromDate:str
    judgeId:  Union[int, str]
    page:int
    serchType:int
    serchTypeValue:str | int
    size:int
    toDate:str

class CaseData(BaseModel):
    caseNumber: str
    complainantName: str
    complainantAdvocateName: Optional[str] = None
    respondentName: str
    respondentAdvocateName: Optional[str] = None
    caseFilingDate: str
    orderDocumentPath: Optional[str] = None
    orderDate: Optional[str] = None
    dateOfDisposal: Optional[str] = None
    caseStageName: Optional[str] = None
    documentBase64: Optional[str] = None
    additionalComplainantList: Optional[List[dict]] = []
    additionalRespondentList: Optional[List[dict]] = []
    additionalComplainant: Optional[str] = None
    additionalRespondent: Optional[str] = None
    orderDocumentBytea: Optional[str] = None
    dailyOrderStatus: Optional[bool] = None
    judgemtmentDocumentPath: Optional[str] = None
    judgemtmentDocumentBytea: Optional[str] = None
    judgemtmentDate: Optional[str] = None
    judgmentOrderDocumentBase64: Optional[str] = None

class CaseDetailsBySearchResponse(BaseModel):
    message: Optional[str] = None
    status: int
    data: Optional[List[CaseData]] = None
    error: Optional[str] = None


class CaseIndustryType(BaseModel):
    caseCategoryId: int
    caseCategoryNameEn: str
        
class CaseCategoryResponse(BaseModel):
    message: str
    status: int
    data: List[CaseIndustryType]
    error: str

class Judge(BaseModel):
    commissionId: int
    courtId: int
    judgeId: int
    judgeName: str
    judgesNameEn: str
    judgesNameLl: str
    justiceStatusId: int
    senioritySequenceId: int

class JudgeList(BaseModel):
    message: str
    status: int
    data: List[Judge]
    error: str     
    

    

class CaseByCaseNumberRequest(BaseModel):
    state:str
    commission:str
    fromDate:str
    toDate:str
    caseNumber:str
class CaseByComplainantRequest(BaseModel):
    state:str
    commission:str
    fromDate:str
    toDate:str
    complainant:str
class CaseByRespondentRequest(BaseModel):
    state:str
    commission:str
    fromDate:str
    toDate:str
    respondent:str
class CaseByComplainantAdvocateRequest(BaseModel):
    state:str
    commission:str
    fromDate:str
    toDate:str
    complainantAdvocate:str
class CaseByRespondentAdvocateRequest(BaseModel):
    state:str
    commission:str
    fromDate:str
    toDate:str
    respondentAdvocate:str
class CaseByIndustryTypeRequest(BaseModel):
    state:str
    commission:str
    fromDate:str
    toDate:str
    industryType:str
class CaseByJudgeRequest(BaseModel):
    state:str
    commission:str
    fromDate:str
    toDate:str
    judge:str
