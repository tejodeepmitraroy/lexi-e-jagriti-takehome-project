
import httpx
from fastapi import HTTPException
from src.commissions.schemas import CommissionResponse

BASE_API_URL = "https://e-jagriti.gov.in/services/report/report/getDistrictCommissionByCommissionId"

async def list_commissions(commission_id: int):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://e-jagriti.gov.in/",
        "Origin": "https://e-jagriti.gov.in",
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(BASE_API_URL + "?commissionId=" + str(commission_id), headers=headers)
            response.raise_for_status()
            data = response.json()
            return CommissionResponse(**data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch states: {e}")