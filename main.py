import datetime
from enum import Enum

from fastapi import FastAPI
from helpers.s3_helpers import S3Helpers

AWS_ACCESS_KEY_ID = 'AKIAYHXUYJPF6UOA5PMZ'
AWS_SECRET_ACCESS_KEY = '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'
BUCKET = 'finance-risk-reporting-files'

"""
TODO:
Add date validator
Separate functions and routes to different files
Load configuration from separate file
"""

class ModelName(str, Enum):
    """Zone enum for validation"""
    ams = "ams"
    nyc = "nyc"
    sng = "sng"


app = FastAPI()
s3_client = S3Helpers(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET)

##########ROUTES

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/vortex/{zone}/{file_date}")
async def read_vortex_file(zone: ModelName, file_date: str):
    key = f"vortex-{zone}-{file_date}.txt"
    body = s3_client.get_object_body()
    return body
