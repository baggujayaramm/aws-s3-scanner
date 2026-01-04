import boto3


def s3_print():
    s3_client=boto3.client('ec2',region_name=
    'us-east-1',aws_access_key_id='',aws_secret_access_key='')
    response = s3_client.list_buckets()
    # print(response["ResponseMetadata"])
    # print(response["Buckets"][0]["Name"])
    for bucket in response['Buckets']:
        print(bucket['CreationDate'])

s3_print()