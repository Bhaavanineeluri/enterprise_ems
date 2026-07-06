from fastapi import FastAPI
from models import *
from database import Base, engine

from routers.auth import router as auth_router
from routers.user_router import router as user_router
from routers.login_history import router as login_history_router
from routers.company import router as company_router
from routers.branch import router as branch_router
from routers.department import router as department_router
from routers.team import router as team_router
from routers.user_assignment import router as user_assignment_router
from routers.user import router as user_router
from











Base.metadata.create_all(bind=engine)

app = FastAPI(title="Enterprise managemnt system API", version="1.0.0")

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(company_router)
app.include_router(branch_router)
app.include_router(department_router)
app.include_router(team_router)
app.include_router(user_assignment_router)
app.include_router(login_history_router)

@app.get("/")
def home():
    return {
        "message": "Enterprise Management System API Running Successfully"
    }