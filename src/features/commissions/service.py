
from src.core.config import global_config
from src.utils.apiClient import apiClient
from .model import CommissionResponse


async def fetch_commission_by_commission_id(commission_id: int):
    data = await apiClient(global_config.BASE_API_URL+ "/report/report/getDistrictCommissionByCommissionId?commissionId=" + str(commission_id)) 
    return  CommissionResponse(**data)