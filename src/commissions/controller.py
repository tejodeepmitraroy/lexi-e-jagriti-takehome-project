from fastapi import HTTPException
from src.core.model import ApiResponse
from src.commissions.model import CommissionResponse
from src.commissions.service import fetch_commission_by_commission_id

async def list_commissions(commission_id: int):

    try:
        commissionData = await fetch_commission_by_commission_id(commission_id)
        
        return ApiResponse(
            statusCode=200,
            message="Commission fetched successfully",
            data=commissionData.data,
            success=True
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
