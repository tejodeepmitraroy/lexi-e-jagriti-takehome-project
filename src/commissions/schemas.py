from typing import List
from pydantic import BaseModel
from src.schemas import CommissionCircuitBench 
       
class CommissionResponse(BaseModel):
    status: int
    error: str   # keep as string because API sends "false" not boolean
    message: str
    data: List[CommissionCircuitBench]