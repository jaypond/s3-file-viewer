import boto3

AWS_ACCESS_KEY_ID = 'AKIAYHXUYJPF6UOA5PMZ'
AWS_SECRET_ACCESS_KEY = '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'


s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

my_file = s3_client.get_object(
    Bucket='finance-risk-reporting-files',
    Key='test.txt'
)

body = my_file['Body'].read().decode('utf-8')

print(body)
