from fastapi import FastAPI

import models
from database import Base, engine

from routers.auth import router as auth_router


from routers.login_history import router as login_history_router







Base.metadata.create_all(bind=engine)

app = FastAPI(title="Enterprise managemnt system API", version="1.0.0")

app.include_router(auth_router)






app.include_router(login_history_router)

@app.get("/")
def home():
    return {
        "message": "Enterprise Management System API Running Successfully"
    }