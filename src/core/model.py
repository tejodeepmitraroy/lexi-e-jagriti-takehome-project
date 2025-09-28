from pydantic import BaseModel
from typing import Optional, Any

class CommissionCircuitBench(BaseModel):
    commissionId: int
    commissionNameEn: str
    circuitAdditionBenchStatus: bool
    activeStatus: bool

class ApiResponse(BaseModel):
    statusCode: int
    message: str
    data: Optional[Any] = None
    success: bool

class ApiError (BaseModel):
    statusCode: int
    message: str
    data: Any
    error: Optional[bool] = False