from typing import List

from fastapi import HTTPException

from src.core.model import ApiResponse
from src.commissions.service import  fetch_commission_by_commission_id
from .model import CaseResponse, CaseByCaseNumberRequest, CaseByComplainantRequest, CaseByRespondentRequest, CaseByComplainantAdvocateRequest, CaseByRespondentAdvocateRequest, CaseByIndustryTypeRequest, CaseByJudgeRequest, CaseDetailsBySearchRequest
from src.states.service import fetch_all_states
from .service import get_case_category, get_case_details_by_search, get_judge_list_for_hearing

async def search_cases_by_case_number(body:CaseByCaseNumberRequest):
    state = body.state
    commission = body.commission
    caseDateType = body.caseDateType
    fromDate = body.fromDate
    toDate = body.toDate
    caseNumber = body.caseNumber
    dateRequestType = 0

    if caseDateType.upper() == "FILING":
        dateRequestType = 1
    elif caseDateType.upper() == "DISPOSAL":
        dateRequestType = 2
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid case date type '{caseDateType}'"
        )

    try:
        # get State Data
        stateData = await fetch_all_states()

        StateResult = next((item for item in stateData.data if item.commissionNameEn and item.commissionNameEn.lower() == state.lower()), None)

        if StateResult:
            commissionId = StateResult.commissionId

            commissionData = await fetch_commission_by_commission_id(commissionId)
            commissionResult = next((item for item in commissionData.data if item.commissionNameEn and item.commissionNameEn.lower() == commission.lower()), None)

            if(commissionResult):
                commissionId = commissionResult.commissionId
            
                caseDetails = await get_case_details_by_search(CaseDetailsBySearchRequest(
                    commissionId=commissionId,
                    dateRequestType=dateRequestType,
                    fromDate=fromDate,
                    toDate=toDate,
                    serchType=1,
                    serchTypeValue=caseNumber,
                    judgeId="",
                    page=0,
                    size=30
                ))

                # Convert API response data to CaseResponse format
                cases:List[CaseResponse] = []
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

                return ApiResponse(
                    statusCode=200,
                    message="Cases are fetched successfully",
                    data=cases,
                    success=True
                )
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
    caseDateType = body.caseDateType
    fromDate = body.fromDate
    toDate = body.toDate
    complainant = body.complainant

    dateRequestType = 0

    if caseDateType.upper() == "FILING":
        dateRequestType = 1
    elif caseDateType.upper() == "DISPOSAL":
        dateRequestType = 2
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid case date type '{caseDateType}'"
        )


    try:
        # get State Data
        stateData = await fetch_all_states()

        StateResult = next((item for item in stateData.data if item.commissionNameEn and item.commissionNameEn.lower() == state.lower()), None)

        if StateResult:
            commissionId = StateResult.commissionId

            commissionData = await fetch_commission_by_commission_id(commissionId)
            commissionResult = next((item for item in commissionData.data if item.commissionNameEn and item.commissionNameEn.lower() == commission.lower()), None)

            if(commissionResult):
                commissionId = commissionResult.commissionId
            
                caseDetails = await get_case_details_by_search(CaseDetailsBySearchRequest(
                    commissionId=commissionId,
                    dateRequestType=dateRequestType,
                    fromDate=fromDate,
                    toDate=toDate,
                    serchType=2,
                    serchTypeValue=complainant,
                    judgeId="",
                    page=0,
                    size=30
                ))

                # Convert API response data to CaseResponse format
                cases:List[CaseResponse] = []
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

                return ApiResponse(
                    statusCode=200,
                    message="Cases are fetched successfully",
                    data=cases,
                    success=True
                )
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
    caseDateType = body.caseDateType

    dateRequestType = 0

    if caseDateType.upper() == "FILING":
        dateRequestType = 1
    elif caseDateType.upper() == "DISPOSAL":
        dateRequestType = 2
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid case date type '{caseDateType}'"
        )


    try:
        # get State Data
        stateData = await fetch_all_states()

        StateResult = next((item for item in stateData.data if item.commissionNameEn and item.commissionNameEn.lower() == state.lower()), None)

        if StateResult:
            commissionId = StateResult.commissionId

            commissionData = await fetch_commission_by_commission_id(commissionId)
            commissionResult = next((item for item in commissionData.data if item.commissionNameEn and item.commissionNameEn.lower() == commission.lower()), None)

            if(commissionResult):
                commissionId = commissionResult.commissionId
            
                caseDetails = await get_case_details_by_search(CaseDetailsBySearchRequest(
                    commissionId=commissionId,
                    dateRequestType=dateRequestType,
                    fromDate=fromDate,
                    toDate=toDate,
                    serchType=3,
                    serchTypeValue=respondent,
                    judgeId="",
                    page=0,
                    size=30
                ))

                # Convert API response data to CaseResponse format
                cases:List[CaseResponse] = []
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

                return ApiResponse(
                    statusCode=200,
                    message="Cases are fetched successfully",
                    data=cases,
                    success=True
                )
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
    caseDateType = body.caseDateType

    dateRequestType = 0

    if caseDateType.upper() == "FILING":
        dateRequestType = 1
    elif caseDateType.upper() == "DISPOSAL":
        dateRequestType = 2
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid case date type '{caseDateType}'"
        )

    try:
        # get State Data
        stateData = await fetch_all_states()

        StateResult = next((item for item in stateData.data if item.commissionNameEn and item.commissionNameEn.lower() == state.lower()), None)

        if StateResult:
            commissionId = StateResult.commissionId

            commissionData = await fetch_commission_by_commission_id(commissionId)
            commissionResult = next((item for item in commissionData.data if item.commissionNameEn and item.commissionNameEn.lower() == commission.lower()), None)

            if(commissionResult):
                commissionId = commissionResult.commissionId
            
                caseDetails = await get_case_details_by_search(CaseDetailsBySearchRequest(
                    commissionId=commissionId,
                    dateRequestType=dateRequestType,
                    fromDate=fromDate,
                    toDate=toDate,
                    serchType=4,
                    serchTypeValue=complainantAdvocate,
                    judgeId="",
                    page=0,
                    size=30
                ))

                # Convert API response data to CaseResponse format
                cases:List[CaseResponse] = []
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

                return ApiResponse(
                    statusCode=200,
                    message="Cases are fetched successfully",
                    data=cases,
                    success=True
                )
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
    caseDateType = req.caseDateType

    dateRequestType = 0

    if caseDateType.upper() == "FILING":
        dateRequestType = 1
    elif caseDateType.upper() == "DISPOSAL":
        dateRequestType = 2
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid case date type '{caseDateType}'"
        )


    try:
        # get State Data
        stateData = await fetch_all_states()

        StateResult = next((item for item in stateData.data if item.commissionNameEn and item.commissionNameEn.lower() == state.lower()), None)

        if StateResult:
            commissionId = StateResult.commissionId

            commissionData = await fetch_commission_by_commission_id(commissionId)
            commissionResult = next((item for item in commissionData.data if item.commissionNameEn and item.commissionNameEn.lower() == commission.lower()), None)

            if(commissionResult):
                commissionId = commissionResult.commissionId
            
                caseDetails = await get_case_details_by_search(CaseDetailsBySearchRequest(
                    commissionId=commissionId,
                    dateRequestType=dateRequestType,
                    fromDate=fromDate,
                    toDate=toDate,
                    serchType=5,
                    serchTypeValue=respondentAdvocate,
                    judgeId="",
                    page=0,
                    size=30
                ))

                # Convert API response data to CaseResponse format
                cases:List[CaseResponse] = []
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

                return ApiResponse(
                    statusCode=200,
                    message="Cases are fetched successfully",
                    data=cases,
                    success=True
                )
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
    caseDateType = req.caseDateType


    dateRequestType = 0

    if caseDateType.upper() == "FILING":
        dateRequestType = 1
    elif caseDateType.upper() == "DISPOSAL":
        dateRequestType = 2
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid case date type '{caseDateType}'"
        )

    try:

        caseCategory = await get_case_category()

        CaseIndustryTypeResult = next((item for item in caseCategory.data if item.caseCategoryNameEn and item.caseCategoryNameEn.lower() == industryType.lower()), None)


        if(CaseIndustryTypeResult):
            # get State Data
            stateData = await fetch_all_states()

            StateResult = next((item for item in stateData.data if item.commissionNameEn and item.commissionNameEn.lower() == state.lower()), None)

            if StateResult:
                commissionId = StateResult.commissionId

                commissionData = await fetch_commission_by_commission_id(commissionId)
                commissionResult = next((item for item in commissionData.data if item.commissionNameEn and item.commissionNameEn.lower() == commission.lower()), None)

                if(commissionResult):
                    commissionId = commissionResult.commissionId

                    caseDetails = await get_case_details_by_search(CaseDetailsBySearchRequest(
                        commissionId=commissionId,
                        dateRequestType=dateRequestType,
                        fromDate=fromDate,
                        toDate=toDate,
                        serchType=6,
                        serchTypeValue=6,
                        judgeId="",
                        page=0,
                        size=30
                    ))

                    # Convert API response data to CaseResponse format
                    cases:List[CaseResponse] = []
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

                    return ApiResponse(
                        statusCode=200,
                        message="Cases are fetched successfully",
                        data=cases,
                        success=True
                    )
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
    caseDateType = req.caseDateType

    dateRequestType = 0

    if caseDateType.upper() == "FILING":
        dateRequestType = 1
    elif caseDateType.upper() == "DISPOSAL":
        dateRequestType = 2
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid case date type '{caseDateType}'"
        )

    try:

        # get State Data
        stateData = await fetch_all_states()

        StateResult = next((item for item in stateData.data if item.commissionNameEn and item.commissionNameEn.lower() == state.lower()), None)

        if StateResult:
            commissionId = StateResult.commissionId

            commissionData = await fetch_commission_by_commission_id(commissionId)
            commissionResult = next((item for item in commissionData.data if item.commissionNameEn and item.commissionNameEn.lower() == commission.lower()), None)

            if(commissionResult):
                commissionId = commissionResult.commissionId

                judgeList = await get_judge_list_for_hearing(commissionId)
                judgeResult = next((item for item in judgeList.data if item.judgeName and item.judgeName.lower() == judgeName.lower()), None)


                if(judgeResult):
                    caseDetails = await get_case_details_by_search(CaseDetailsBySearchRequest(
                        commissionId=commissionId,
                        dateRequestType=dateRequestType,
                        fromDate=fromDate,
                        toDate=toDate,
                        serchType=7,
                        serchTypeValue=7,
                        judgeId=judgeResult.judgeId,
                        page=0,
                        size=30
                    ))
                    # print(caseDetails.data)

                    # Convert API response data to CaseResponse format
                    cases:List[CaseResponse] = []
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

                    return ApiResponse(
                        statusCode=200,
                        message="Cases are fetched successfully",
                        data=cases,
                        success=True
                    )
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
   

