import boto3

def lambda_handler(event, context):
    result = "Changed Result"
    return {
        'statusCode' : 200,
        'body': result
    }