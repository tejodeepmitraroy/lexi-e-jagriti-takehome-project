from src.config import global_config
from src.utils.apiClient import apiClient
from .schemas import StateResponse
from fastapi import HTTPException

async def get_all_states():

   try:
      data = await apiClient(global_config.BASE_API_URL+"/report/report/getStateCommissionAndCircuitBench") 
      return StateResponse(**data)
   except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))