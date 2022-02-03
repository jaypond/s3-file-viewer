import boto3

class S3Helpers():
    def __init__(self, aws_access_key_id, aws_secret_access_key, bucket):
        self.client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        self.bucket = bucket

    def get_object_body(key: str):
        """
        Retrieve the body of an object using the key.
        """
        obj = s3_client.get_object(
            Bucket=self.bucket,
            Key=key
        )
        body = obj['Body'].read().decode('utf-8')

        return body
