from .model import CaseDetailsBySearchResponse, CaseDetailsBySearchRequest, CaseCategoryResponse, Judge, JudgeList
from src.core.config import global_config
from src.utils.apiClient import apiClient

async def get_case_details_by_search(data:CaseDetailsBySearchRequest) -> CaseDetailsBySearchResponse:
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


async def get_case_category():
    caseCategory = await apiClient(global_config.BASE_API_URL+ "/master/master/v2/caseCategory",method="POST",data={
        "caseCategoryLevel": 1,
        "parentCaseCategoryId": 0
    })

    return CaseCategoryResponse(**caseCategory)
    
async def get_judge_list_for_hearing(commissionId:int):
    url = f"{global_config.BASE_API_URL}/master/master/v2/getJudgeListForHearing?commissionId={commissionId}&activeStatus=true"
    judgeList = await apiClient(url,method="POST",data={})

    return JudgeList(**judgeList)