import boto3
import logging 
import os
from botocore.exceptions import ClientError

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket
    
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    if object_name is None:
      object_name = os.path.basename(file_name)
      
    s2_client = boto3.client("s3")
    
    try:
      response = s2_client.upload_file(file_name, bucket, object_name)
    
    except ClientError as e:
      logging.error(e)
      return False
    
    return True

if __name__ == "__main__":
  upload_file("functions.py", "gloxon", "functions.py")  
  
  
def download_file():
  pass