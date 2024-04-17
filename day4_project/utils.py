import boto3

def get_instance(response) -> dict:
  """ Uses the response from boto3_client.describe_instances to extract the single instance data in it
  
  Args:
      response (dict): Response from boto3_client.describe_instances
      
  Returns:
      dict: Dict containing data related to a single instance
  
  """
    
  instances = ["Reservations"][0]["Instances"]
  instance = instances[0]
  return instance
  
  
  def get_instance_tags():
    """Extracts all tags from an AWS instance
    
    Args:
      instance (dict): Json data containing instance infor
        
    Returns
      list: List of instance tags     
    """
      
  return instance["Tags"]

def format_tag(value) -> str:
  """Formats the tag to meet up with company's tagging policy
  
  Args:
      value (str): Tag value from aws
      
  Returns:
      str: Formatted tag value
  
  """
  value = value.lower().replace(" ", "_")
  return value

def send_sns_notification(instance_id, tags_to_create) -> None:
  """Sends an SNS notification to the company's SNS topic
  
  Args:
      instance_id (str): The instance id
      tags_to_create (list): List of tags to create
  
  """
  subject = f"Policia violation on Instance {instance_id}"
  message = """
  Hello,

    one of the instances created in your environment doesn't respect the tagging standards.
    The instance has been automatically updated with the required tags. The tags created are:

    {tags_to_create}

    Regards
    AWS Policia
  """
  topic_arn = ""
  sns_client = boto3.client('sns')
  sns_client.publish(Subject=subject, Message=message, Topic=topic_arn)