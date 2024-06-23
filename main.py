from fastapi import FastAPI
from sql_app.router import router as auth_router

app = FastAPI()
app.include_router(auth_router,prefix="/auth",tags=['authentication'])


