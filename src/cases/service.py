from typing import List

from fastapi import HTTPException

from src.commissions.service import list_commissions
from .schemas import CaseByCaseNumberRequest, CaseCategoryResponse, CaseDetailsBySearchResponse, CaseResponse, CaseByComplainantRequest, CaseByRespondentRequest, CaseByComplainantAdvocateRequest, CaseByRespondentAdvocateRequest, CaseByIndustryTypeRequest, CaseByJudgeRequest, CaseDetailsBySearchRequest, JudgeList
from src.states.service import get_all_states
from src.utils.apiClient import apiClient
from src.config import global_config


async def getCaseDetailsBySearch(data:CaseDetailsBySearchRequest) -> CaseDetailsBySearchResponse:
    body = {
        "commissionId": data.commissionId,
        "dateRequestType": data.dateRequestType,
        "fromDate": data.fromDate,
        "judgeId": data.judgeId,
        "page": data.page,
        "serchType": data.serchType,
        "serchTypeValue": data.serchTypeValue,
        "size": data.size,
        "toDate": data.toDate,
    }
    

    case = await apiClient(global_config.BASE_API_URL+ "/case/caseFilingService/v2/getCaseDetailsBySearchType",method="POST",data=body)

    # Convert the raw API response to our Pydantic model
    return CaseDetailsBySearchResponse(**case)


async def getCaseCategory():
    caseCategory = await apiClient(global_config.BASE_API_URL+ "/master/master/v2/caseCategory",method="POST",data={
        "caseCategoryLevel": 1,
        "parentCaseCategoryId": 0
    })

    return CaseCategoryResponse(**caseCategory)
    
async def getJudgeListForHearing(commissionId:int):
    url = f"{global_config.BASE_API_URL}/master/master/v2/getJudgeListForHearing?commissionId={commissionId}&activeStatus=true"
    judgeList = await apiClient(url,method="POST",data={})

    return JudgeList(**judgeList)

async def search_cases_by_case_number(body:CaseByCaseNumberRequest) -> List[CaseResponse]:
    state = body.state
    commission = body.commission
    fromDate = body.fromDate
    toDate = body.toDate
    caseNumber = body.caseNumber

    try:
        # get State Data
        stateData = await get_all_states()

        StateResult = next((item for item in stateData.data if item.commissionNameEn and item.commissionNameEn.lower() == state.lower()), None)

        if StateResult:
            commissionId = StateResult.commissionId

            commissionData = await list_commissions(commissionId)
            commissionResult = next((item for item in commissionData.data if item.commissionNameEn and item.commissionNameEn.lower() == commission.lower()), None)

            if(commissionResult):
                commissionId = commissionResult.commissionId
            
                caseDetails = await getCaseDetailsBySearch(CaseDetailsBySearchRequest(
                    commissionId=commissionId,
                    dateRequestType=1,
                    fromDate=fromDate,
                    toDate=toDate,
                    serchType=1,
                    serchTypeValue=caseNumber,
                    judgeId="",
                    page=0,
                    size=30
                ))

                # Convert API response data to CaseResponse format
                cases = []
                for case in caseDetails.data:
                    cases.append(CaseResponse(
                        case_number=case.caseNumber,
                        case_stage=case.caseStageName,
                        filing_date=case.caseFilingDate,
                        complainant=case.complainantName,
                        complainant_advocate=case.complainantAdvocateName,
                        respondent=case.respondentName,
                        respondent_advocate=case.respondentAdvocateName,
                        document_link=case.orderDocumentPath
                    ))

                return cases
            else:
                raise HTTPException(
                    status_code=400,
                    detail=f"Commission '{commission}' not found for state '{state}'"
                )
        else:
            raise HTTPException(
                status_code=400,
                detail=f"State '{state}' not found"
            )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def search_cases_by_complainant(body: CaseByComplainantRequest) -> List[CaseResponse]:
    state = body.state
    commission = body.commission
    fromDate = body.fromDate
    toDate = body.toDate
    complainant = body.complainant

    try:
        # get State Data
        stateData = await get_all_states()

        StateResult = next((item for item in stateData.data if item.commissionNameEn and item.commissionNameEn.lower() == state.lower()), None)

        if StateResult:
            commissionId = StateResult.commissionId

            commissionData = await list_commissions(commissionId)
            commissionResult = next((item for item in commissionData.data if item.commissionNameEn and item.commissionNameEn.lower() == commission.lower()), None)

            if(commissionResult):
                commissionId = commissionResult.commissionId
            
                caseDetails = await getCaseDetailsBySearch(CaseDetailsBySearchRequest(
                    commissionId=commissionId,
                    dateRequestType=1,
                    fromDate=fromDate,
                    toDate=toDate,
                    serchType=2,
                    serchTypeValue=complainant,
                    judgeId="",
                    page=0,
                    size=30
                ))

                # Convert API response data to CaseResponse format
                cases = []
                for case in caseDetails.data:
                    cases.append(CaseResponse(
                        case_number=case.caseNumber,
                        case_stage=case.caseStageName,
                        filing_date=case.caseFilingDate,
                        complainant=case.complainantName,
                        complainant_advocate=case.complainantAdvocateName,
                        respondent=case.respondentName,
                        respondent_advocate=case.respondentAdvocateName,
                        document_link=case.orderDocumentPath
                    ))

                return cases
            else:
                raise HTTPException(
                    status_code=400,
                    detail=f"Commission '{commission}' not found for state '{state}'"
                )
        else:
            raise HTTPException(
                status_code=400,
                detail=f"State '{state}' not found"
            )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
   
async def search_cases_by_respondent(body: CaseByRespondentRequest) -> List[CaseResponse]:
    state = body.state
    commission = body.commission
    fromDate = body.fromDate
    toDate = body.toDate
    respondent = body.respondent

    try:
        # get State Data
        stateData = await get_all_states()

        StateResult = next((item for item in stateData.data if item.commissionNameEn and item.commissionNameEn.lower() == state.lower()), None)

        if StateResult:
            commissionId = StateResult.commissionId

            commissionData = await list_commissions(commissionId)
            commissionResult = next((item for item in commissionData.data if item.commissionNameEn and item.commissionNameEn.lower() == commission.lower()), None)

            if(commissionResult):
                commissionId = commissionResult.commissionId
            
                caseDetails = await getCaseDetailsBySearch(CaseDetailsBySearchRequest(
                    commissionId=commissionId,
                    dateRequestType=1,
                    fromDate=fromDate,
                    toDate=toDate,
                    serchType=3,
                    serchTypeValue=respondent,
                    judgeId="",
                    page=0,
                    size=30
                ))

                # Convert API response data to CaseResponse format
                cases = []
                for case in caseDetails.data:
                    cases.append(CaseResponse(
                        case_number=case.caseNumber,
                        case_stage=case.caseStageName,
                        filing_date=case.caseFilingDate,
                        complainant=case.complainantName,
                        complainant_advocate=case.complainantAdvocateName,
                        respondent=case.respondentName,
                        respondent_advocate=case.respondentAdvocateName,
                        document_link=case.orderDocumentPath
                    ))

                return cases
            else:
                raise HTTPException(
                    status_code=400,
                    detail=f"Commission '{commission}' not found for state '{state}'"
                )
        else:
            raise HTTPException(
                status_code=400,
                detail=f"State '{state}' not found"
            )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
   

async def search_cases_by_complainant_advocate(body: CaseByComplainantAdvocateRequest) -> List[CaseResponse]:
    state = body.state
    commission = body.commission
    fromDate = body.fromDate
    toDate = body.toDate
    complainantAdvocate = body.complainantAdvocate

    try:
        # get State Data
        stateData = await get_all_states()

        StateResult = next((item for item in stateData.data if item.commissionNameEn and item.commissionNameEn.lower() == state.lower()), None)

        if StateResult:
            commissionId = StateResult.commissionId

            commissionData = await list_commissions(commissionId)
            commissionResult = next((item for item in commissionData.data if item.commissionNameEn and item.commissionNameEn.lower() == commission.lower()), None)

            if(commissionResult):
                commissionId = commissionResult.commissionId
            
                caseDetails = await getCaseDetailsBySearch(CaseDetailsBySearchRequest(
                    commissionId=commissionId,
                    dateRequestType=1,
                    fromDate=fromDate,
                    toDate=toDate,
                    serchType=4,
                    serchTypeValue=complainantAdvocate,
                    judgeId="",
                    page=0,
                    size=30
                ))

                # Convert API response data to CaseResponse format
                cases = []
                for case in caseDetails.data:
                    cases.append(CaseResponse(
                        case_number=case.caseNumber,
                        case_stage=case.caseStageName,
                        filing_date=case.caseFilingDate,
                        complainant=case.complainantName,
                        complainant_advocate=case.complainantAdvocateName,
                        respondent=case.respondentName,
                        respondent_advocate=case.respondentAdvocateName,
                        document_link=case.orderDocumentPath
                    ))

                return cases
            else:
                raise HTTPException(
                    status_code=400,
                    detail=f"Commission '{commission}' not found for state '{state}'"
                )
        else:
            raise HTTPException(
                status_code=400,
                detail=f"State '{state}' not found"
            )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def search_cases_by_respondent_advocate(req: CaseByRespondentAdvocateRequest) -> List[CaseResponse]:
    state = req.state
    commission = req.commission
    fromDate = req.fromDate
    toDate = req.toDate
    respondentAdvocate = req.respondentAdvocate

    try:
        # get State Data
        stateData = await get_all_states()

        StateResult = next((item for item in stateData.data if item.commissionNameEn and item.commissionNameEn.lower() == state.lower()), None)

        if StateResult:
            commissionId = StateResult.commissionId

            commissionData = await list_commissions(commissionId)
            commissionResult = next((item for item in commissionData.data if item.commissionNameEn and item.commissionNameEn.lower() == commission.lower()), None)

            if(commissionResult):
                commissionId = commissionResult.commissionId
            
                caseDetails = await getCaseDetailsBySearch(CaseDetailsBySearchRequest(
                    commissionId=commissionId,
                    dateRequestType=1,
                    fromDate=fromDate,
                    toDate=toDate,
                    serchType=5,
                    serchTypeValue=respondentAdvocate,
                    judgeId="",
                    page=0,
                    size=30
                ))

                # Convert API response data to CaseResponse format
                cases = []
                for case in caseDetails.data:
                    cases.append(CaseResponse(
                        case_number=case.caseNumber,
                        case_stage=case.caseStageName,
                        filing_date=case.caseFilingDate,
                        complainant=case.complainantName,
                        complainant_advocate=case.complainantAdvocateName,
                        respondent=case.respondentName,
                        respondent_advocate=case.respondentAdvocateName,
                        document_link=case.orderDocumentPath
                    ))

                return cases
            else:
                raise HTTPException(
                    status_code=400,
                    detail=f"Commission '{commission}' not found for state '{state}'"
                )
        else:
            raise HTTPException(
                status_code=400,
                detail=f"State '{state}' not found"
            )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 
async def search_cases_by_industry_type(req: CaseByIndustryTypeRequest) -> List[CaseResponse]:
    state = req.state
    commission = req.commission
    fromDate = req.fromDate
    toDate = req.toDate
    industryType = req.industryType
    try:

        caseCategory = await getCaseCategory()

        CaseIndustryTypeResult = next((item for item in caseCategory.data if item.caseCategoryNameEn and item.caseCategoryNameEn.lower() == industryType.lower()), None)


        if(CaseIndustryTypeResult):
            # get State Data
            stateData = await get_all_states()

            StateResult = next((item for item in stateData.data if item.commissionNameEn and item.commissionNameEn.lower() == state.lower()), None)

            if StateResult:
                commissionId = StateResult.commissionId

                commissionData = await list_commissions(commissionId)
                commissionResult = next((item for item in commissionData.data if item.commissionNameEn and item.commissionNameEn.lower() == commission.lower()), None)

                if(commissionResult):
                    commissionId = commissionResult.commissionId


                
                    caseDetails = await getCaseDetailsBySearch(CaseDetailsBySearchRequest(
                        commissionId=commissionId,
                        dateRequestType=2,
                        fromDate=fromDate,
                        toDate=toDate,
                        serchType=6,
                        serchTypeValue=6,
                        judgeId="",
                        page=0,
                        size=30
                    ))

                    # Convert API response data to CaseResponse format
                    cases = []
                    for case in caseDetails.data:
                        cases.append(CaseResponse(
                            case_number=case.caseNumber,
                            case_stage=case.caseStageName,
                            filing_date=case.caseFilingDate,
                            complainant=case.complainantName,
                            complainant_advocate=case.complainantAdvocateName,
                            respondent=case.respondentName,
                            respondent_advocate=case.respondentAdvocateName,
                            document_link=case.orderDocumentPath
                        ))

                    return cases
                else:
                    raise HTTPException(
                        status_code=400,
                        detail=f"Commission '{commission}' not found for state '{state}'"
                    )
            else:
                raise HTTPException(
                    status_code=400,
                    detail=f"State '{state}' not found"
                ) 
        else:
            validIndustryType = [ case.caseCategoryNameEn for case in caseCategory.data if case.caseCategoryNameEn ] 
            raise HTTPException(
                status_code=400,
                detail=f"Industry Type '{industryType}' not found please enter valid industry type from list:{validIndustryType}"
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 
async def search_cases_by_judge(req: CaseByJudgeRequest) -> List[CaseResponse]:
   
    state = req.state
    commission = req.commission
    fromDate = req.fromDate
    toDate = req.toDate
    judgeName = req.judge
    try:

        # get State Data
        stateData = await get_all_states()

        StateResult = next((item for item in stateData.data if item.commissionNameEn and item.commissionNameEn.lower() == state.lower()), None)

        if StateResult:
            commissionId = StateResult.commissionId

            commissionData = await list_commissions(commissionId)
            commissionResult = next((item for item in commissionData.data if item.commissionNameEn and item.commissionNameEn.lower() == commission.lower()), None)

            if(commissionResult):
                commissionId = commissionResult.commissionId

                judgeList = await getJudgeListForHearing(commissionId)
                judgeResult = next((item for item in judgeList.data if item.judgeName and item.judgeName.lower() == judgeName.lower()), None)


                if(judgeResult):
                    
                    caseDetails = await getCaseDetailsBySearch(CaseDetailsBySearchRequest(
                        commissionId=commissionId,
                        dateRequestType=2,
                        fromDate=fromDate,
                        toDate=toDate,
                        serchType=7,
                        serchTypeValue=7,
                        judgeId=judgeResult.judgeId,
                        page=0,
                        size=30
                    ))

                    # Convert API response data to CaseResponse format
                    cases = []
                    for case in caseDetails.data:
                        cases.append(CaseResponse(
                            case_number=case.caseNumber,
                            case_stage=case.caseStageName,
                            filing_date=case.caseFilingDate,
                            complainant=case.complainantName,
                            complainant_advocate=case.complainantAdvocateName,
                            respondent=case.respondentName,
                            respondent_advocate=case.respondentAdvocateName,
                            document_link=case.orderDocumentPath
                        ))

                    return cases
                else:
                    raise HTTPException(
                        status_code=400,
                        detail=f"Judge '{judgeName}' not found for commission '{commission}' "
                    )
            else:
                raise HTTPException(
                    status_code=400,
                    detail=f"Commission '{commission}' not found for state '{state}'"
                )
        else:
            raise HTTPException(status_code=400,detail=f"State '{state}' not found")      
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
   

