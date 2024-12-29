import json
import dev-01

def lambda_handler(event,context):
    client = boto3.client('ec2')
    response=client.run_instances(
        ImageID='ami-0614680123427b75e'
        InstanceType='t2.micro',
        KeyName='mykeymumbai',
        MaxCount=1,
        MinCount=1
)
