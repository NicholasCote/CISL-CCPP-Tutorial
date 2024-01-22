# os is used to get local environment variables 
import os
# boto3 is the python package used to interact with S3
import boto3
import botocore
# This requests package is imported to disable certificate access warnings. 
# SSL certificates can be provided and this would not be required.
import requests.packages.urllib3
# We aren't verifying certs to start so this line is disable warnings
requests.packages.urllib3.disable_warnings()

# Define the Stratus S3 client to be used in other operations
def stratus_s3_client():
    # Define the API endpoint for stratus
    endpoint = "https://stratus.ucar.edu/"
    # Create a boto3 sessions
    session = boto3.session.Session()
    # Create the S3 client based on the variables we set and provided
    s3_client = session.client(
        service_name='s3', 
        endpoint_url=endpoint, 
        verify=False)
    # Return the client so that it can be used in other functions
    return s3_client
    
# Define the Stratus S3 resource to be used in other operations    
def stratus_s3_resource():
    # Define the API endpoint for stratus
    endpoint = "https://stratus.ucar.edu/"
    # Create a boto3 sessions
    session = boto3.session.Session()
    # Create the S3 resource based on the variables we set and provided
    s3_resource = session.resource(
        service_name='s3', 
        endpoint_url=endpoint, 
        verify=False)
    # Return the client so that it can be used in other functions
    return s3_resource
    
# Define a function to upload a file/object to a bucket, specify the filename to upload and the bucket name to be placed in
def upload_file(filename, bucketname, objectname):
    # Use the S3 client already defined to make the call
    s3_client = stratus_s3_client()
    # Use the upload_file endpoint to upload our filename to the specified bucket and keep the filename the same
    s3_client.upload_file(filename, bucketname, objectname)
    print('Done!')

# Define a function to list all the objects stored in a bucket
def list_bucket_objs(bucket):
    # Use the S3 resource already defined to make the call
    s3_resource = stratus_s3_resource()
    # Get the individual bucket resources for the bucket name provided in the function 
    bucket = s3_resource.Bucket(bucket)
    # Iterate through the response to show all objects contained within the bucket
    for obj in bucket.objects.all():
        print(obj.key)