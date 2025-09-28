from fastapi import HTTPException
from src.core.model import ApiError, ApiResponse
from src.states.service import fetch_all_states
from .model import StateCommissionResponse



async def get_all_states():

   try:
      stateData = await fetch_all_states()
      
      return ApiResponse(
         statusCode=200,
         message="All States fetched successfully",
         data=stateData.data,
         success=True
      )
   except Exception as e:
      raise HTTPException(
         status_code=500,
         detail=str(e)
      )