from helpers.aws_helpers import S3Helpers
from loguru import logger

AWS_ACCESS_KEY_ID = 'AKIAYHXUYJPF6UOA5PMZ'
AWS_SECRET_ACCESS_KEY = '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'
BUCKET = 'finance-risk-reporting-files'

async def get_s3_client():
    """
    TODO: Load secrets via environment variables. Maybe K8 secrets mounted
    as env variables
    """
    logger.info('HERE S3 CLIENT')
    s3_client = S3Helpers(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET)
    return s3_client
