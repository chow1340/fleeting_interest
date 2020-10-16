import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

S3_ACCESSKEY = os.environ.get("S3_ACCESSKEY")
S3_SECRETKEY = os.environ.get("S3_SECRETKEY")
S3_BUCKETNAME = os.environ.get("S3_BUCKETNAME")