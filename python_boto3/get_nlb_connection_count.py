import boto3
from datetime import datetime
from datetime import timedelta

def get_nlb_connection_avg(nlb_name):
    client = boto3.client('cloudwatch')
    response = client.get_metric_statistics(
        Namespace='AWS/NetworkELB',
        MetricName='NewFlowCount',
        Dimensions=[
            {
                'Name': 'LoadBalancer',
                'Value': nlb_name
            },
            {
                'Name': 'AvailabilityZone',
                'Value': 'us-west-2a'
            }
        ],
        StartTime=datetime.utcnow() - timedelta(days=5),
        EndTime=datetime.utcnow() - timedelta(days=1),
        Period=3600,
        Statistics=[
            'Average',
        ],
        
)    

    sum_count = 0
    avg_count = 0
    for count in response['Datapoints']:
        sum_count += count['Average'] 
        avg_count += 1
        # print(count['Average'])
    avg =  sum_count/avg_count
    return(avg)

nlb_client = boto3.client('elbv2')

nlb_response = nlb_client.describe_load_balancers()
for nlb_item in nlb_response['LoadBalancers']:
    if nlb_item[ 'Type'] != 'network':
        continue
    nlb_arn_split_list = nlb_item['LoadBalancerArn'].split(':')[5]
    nlb_arn_split_list = arn_split_list.split('/')
    nlb_name = f"{nlb_arn_split_list[1]}/{nlb_arn_split_list[2]}/{nlb_arn_split_list[3]}"
    response = f"Loadbalancer,ConnectionAverage\n{nlb_name},{get_nlb_connection_avg(nlb_name)}"
    print(response)
