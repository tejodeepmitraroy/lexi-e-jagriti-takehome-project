from pydantic import BaseModel

class CommissionCircuitBench(BaseModel):
    commissionId: int
    commissionNameEn: str
    circuitAdditionBenchStatus: bool
    activeStatus: bool