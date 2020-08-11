import boto3
from operator import itemgetter

'''
filters = [ {
    'Name': 'name',
    'Values': ['amzn-ami-hvm-*']
},{
    'Name': 'description',
    'Values': ['Amazon Linux AMI*']
},{
    'Name': 'architecture',
    'Values': ['x86_64']
},{
    'Name': 'owner-alias',
    'Values': ['amazon']
},{
    'Name': 'owner-id',
    'Values': ['137112412989']
},{
    'Name': 'state',
    'Values': ['available']
},{
    'Name': 'root-device-type',
    'Values': ['ebs']
},{
    'Name': 'virtualization-type',
    'Values': ['hvm']
},{
    'Name': 'hypervisor',
    'Values': ['xen']
},{
    'Name': 'image-type',
    'Values': ['machine']
} ]

'''
client = boto3.client('ec2')
ami_names = ["ami-name-1","ami-name-2"]
for name in ami_names:
    response = client.describe_images(
    Filters=[
        {
            'Name': 'name',
            'Values': [str(name)]
        },
    ]
)
    # Sort on Creation date Desc
    image_details = sorted(response['Images'],key=itemgetter('CreationDate'),reverse=True)
    ami_id = image_details[0]['ImageId']
    print(ami_id)
