from src.commissions.schemas import CommissionResponse
from src.utils.apiClient import apiClient
from src.config import global_config

async def list_commissions(commission_id: int):
    data = await apiClient(global_config.BASE_API_URL+ "/report/report/getDistrictCommissionByCommissionId?commissionId=" + str(commission_id)) 
    return CommissionResponse(**data)