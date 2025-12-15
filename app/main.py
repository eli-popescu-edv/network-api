from fastapi import FastAPI
from app.routers import subnet_calculator, net_tools

app = FastAPI()

app.include_router(subnet_calculator.router)
app.include_router(net_tools.router)
