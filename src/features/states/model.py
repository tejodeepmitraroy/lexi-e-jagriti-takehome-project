from typing import List
from pydantic import BaseModel
from src.core.model import CommissionCircuitBench 
       
class StateCommissionResponse(BaseModel):
    status: int
    error: str   # keep as string because API sends "false" not boolean
    message: str
    data: List[CommissionCircuitBench]