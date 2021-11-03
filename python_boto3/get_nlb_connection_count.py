import boto3
from datetime import datetime
from datetime import timedelta

def get_nlb_connection_avg(nlb_name,az):
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
                'Value': az
            },
            
            # {
            #     'Name': 'AvailabilityZone',
            #     'Value': 'us-west-2b'
            # }
        ],
        StartTime=datetime.utcnow() - timedelta(days=30),
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
    try:
        avg =  sum_count/avg_count
    except:
        print("No historic data")
    return(avg)

nlb_client = boto3.client('elbv2')

nlb_response = nlb_client.describe_load_balancers()
print("Loadbalancer,ConnectionAverage")
for nlb_item in nlb_response['LoadBalancers']:
    # print(nlb_item)
    if nlb_item[ 'Type'] != 'network':
        continue
    for az in nlb_item['AvailabilityZones']:
       arn_split_list = nlb_item['LoadBalancerArn'].split(':')[5]
       arn_split_list = arn_split_list.split('/')
       nlb_name = f"{arn_split_list[1]}/{arn_split_list[2]}/{arn_split_list[3]}"
       response = f"{nlb_name},{get_nlb_connection_avg(nlb_name,az['ZoneName'])}"
       print(response)
