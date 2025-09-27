from fastapi import FastAPI
from src.states.router import router as states_router
from src.commissions.router import router as commissions_router
from src.cases.router import router as cases_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="My Feature-Based API", description="API for managing features", version="1.0.0", openapi_tags=[
    {
        "name": "states",
        "description": "States related operations"
    }
])

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Server Health Check
@app.get("/", tags=["health_check"])
def server_health_check():
    return {"message": "Server is 100% running"}

#API Routers
app.include_router(states_router)
app.include_router(commissions_router)
app.include_router(cases_router)


