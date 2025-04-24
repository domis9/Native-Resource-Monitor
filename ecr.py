#create ecr repo using py
import boto3

ecr_client = boto3.client('ecr')

repository_name = "native_monitor"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)