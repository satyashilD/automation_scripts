import json
import boto3

client = boto3.client('ec2',region_name='eu-west-2')
ec2 = boto3.resource('ec2',region_name='eu-west-2')

#FOr starting instances based on tags
def start_instances():
    instances = ec2.instances.filter(Filters=[{'Name':'tag:scheduler', 'Values':['yes']}])
    for instance in instances:
        print("Starting instance:", instance.id)
        response = client.start_instances( InstanceIds=[instance.id] )

# For stopping instance based on tags
def start_instances():
    instances = ec2.instances.filter(Filters=[{'Name':'tag:scheduler', 'Values':['yes']}])
    for instance in instances:
        print("Starting instance:", instance.id)
        response = client.start_instances( InstanceIds=[instance.id] )

#start_instances()
stop_instances()
