from src.utils.apiClient import apiClient
from src.core.config import global_config
from .model import StateCommissionResponse

async def fetch_all_states():
   data = await apiClient(global_config.BASE_API_URL+"/report/report/getStateCommissionAndCircuitBench") 
   return StateCommissionResponse(**data)