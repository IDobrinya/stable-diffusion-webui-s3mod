
import boto3
from botocore.client import Config

from modules.env_to_yaml import get_env_var

s3_client = boto3.client(
    's3',
    endpoint_url=get_env_var(key="S3_ENDPOINT"),
    aws_access_key_id=get_env_var(key="S3_ACCESS_KEY"),
    aws_secret_access_key=get_env_var(key="S3_SECRET_ACCESS_KEY"),
    region_name='ru-1',
    config=Config(s3={'addressing_style': 'path'})
)
