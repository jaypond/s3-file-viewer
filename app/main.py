import datetime

from enum import Enum
from loguru import logger

from fastapi import FastAPI, Depends
from dependencies import get_s3_client


"""
TODO:
Add date validator
Separate functions and routes to different files
Load configuration from separate file
"""

class VortexZones(str, Enum):
    """Zone enum for validation"""
    ams = "ams"
    nyc = "nyc"
    sng = "sng"

class FinanceZones(str, Enum):
    """Zone enum for validation"""
    aml = "aml"
    nyq = "nyq"
    sgl = "sgl"


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/vortex/{zone}/{file_date}")
async def read_vortex_file(zone: VortexZones, file_date: str, s3_client=Depends(get_s3_client)):
    key = f"vortex-{zone}-{file_date}.txt"
    body = s3_client.get_object_body(key)
    return body

@app.get("/finance/{zone}/{file_date}")
async def read_finance_file(zone: FinanceZones, file_date: str, s3_client=Depends(get_s3_client)):
    key = f"finance-{zone}-{file_date}.txt"
    body = s3_client.get_object_body(key)
    return body
