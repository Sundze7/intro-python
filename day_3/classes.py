import boto3
import logging
import os
from botocore.exceptions import ClientError

class S3FileManager:
  
  def __init__(self, bucket_name):
    self.bucket_name = bucket_name
    self.client = boto3.client("s3")
  
  def upload_file(self,file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket
    
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    if object_name is None:
      object_name = os.path.basename(file_name)
      
    try:
      # code to run
      response = self.client.upload_file(file_name, bucket, object_name)
    
    except ClientError as e:
      # code to run if exception occurs
      logging.error(e)
      return False
    
    return True
  
  def download_file(file_name, bucket, object_name):
    """Download a file from an S3 bucket
    
    :param file_name: File to download
    :param bucket: Bucket to download from
    :param object_name: S3 object name
    :return: True if file was downloaded, else False
    """
    s3 = boto3.client("s3")
    
    try:
      s3.download_file(bucket, object_name, file_name)
      
    except ClientError as e:
      logging.error(e)
      return False
    
