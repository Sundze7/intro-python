import boto3
import utils

REQUIRED_TAGS = {"environment": "prod", "resource": "project", "team": "default"}

def lambda_handler(event, context):
  client = boto3.client("ec2")
  
  instance_id = event["detail"]["instance-id"]
  
  # Describe
  response = client.describe_instances(InstanceIds=[instance_id])
  
  instance = utils.get_instance(response)
  tags = utils.get_instance_tags(instance)
  
  to_update = []
  to_create = []
  keys = []
  
  for tag in tags:
    key = tag["Key"]
    value = tag["Value"]
    value = utils.format_tag(value)
    to_update.append({"Key": key, "Value": value})
    keys.append(key.lower())
    
  required_tags_keys = REQUIRED_TAGS.keys()
  
  for key in required_tags_keys:
    if not key.lower() in keys:
      to_create.append({"Key": key, "Value": REQUIRED_TAGS[key]})
      
  tags = to_create + to_update
  
  client.create_tags(Resources=[instance_id], Tags=tags)
  
  if len(to_create) > 0:
    utils.send_sns_notification(instance_id, to_create)
    
# if __name__ == '__main__':
#   event = {
#     "version":"0",
#     "id":"cc17fef3-589d-d1cf-d08d-e56196681c61",
#     "detail-type":"EC2 Instance State-change Notification",
#     "source":"aws.ec2",
#     "account":"345331916214",
#     "time":"2023-10-14T01:41:11Z",
#     "region":"us-east-2",
#     "resources":[
#       "arn:aws:ec2:us-east-2:345331916214:instance/i-07cc0ef69157ea3e1"
#     ],
#     "detail":{
#       "instance-id":"i-0d8f81b58fc7303cc",
#       "state":"pending"
#     }
#   }
  
#   context = {}
#   lambda_handler(event, context)
  
  
