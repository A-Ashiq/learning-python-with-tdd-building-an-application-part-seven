from fastapi import FastAPI
from .routers import taxes

app = FastAPI()
app.include_router(router=taxes.router)
