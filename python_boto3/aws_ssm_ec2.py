import boto3

def execute_commands_on_linux_instances(client, commands, instance_ids):
    """Runs commands on remote linux instances
    :param client: a boto/boto3 ssm client
    :param commands: a list of strings, each one a command to execute on the instances
    :param instance_ids: a list of instance_id strings, of the instances on which to execute the command
    :return: the response from the send_command function (check the boto3 docs for ssm client.send_command() )
    """

    resp = client.send_command(
        DocumentName="AWS-RunShellScript", # One of AWS' preconfigured documents
        Parameters={'commands': commands},
        InstanceIds=instance_ids,
    )
    return resp

# Example use:
ssm_client = boto3.client('ssm',aws_access_key_id='XXXXX',
    aws_secret_access_key='XXXXX', region_name='us-east-2') # Need your credentials here
var = ''' echo #!/bin/bash
free -m >>/var/log/memory_log'''
var2 = ''' echo #!/bin/bash
ls -lrth /tmp >> /tmp/satya
sudo apt-get install apache2 -y >> /tmp/satya
sudo service apache2 start
sudo service apache2 status'''
commands = ['echo' + var2 + ' >> /tmp/satya']
instance_ids = ['i-064a7368b3926b57a']
execute_commands_on_linux_instances(ssm_client, commands, instance_ids)
