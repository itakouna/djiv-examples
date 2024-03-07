import boto3
import os


def send_message_sqs(message):
    # Create a session using AWS SDK
    session = boto3.Session(
        aws_access_key_id=os.environ.get('ACCESS_KEY'),
        aws_secret_access_key=os.environ.get('SECRET_KEY'),
        region_name='us-east-1'
    )

    # Create an SQS client
    sqs = session.client('sqs')

    # Specify your SQS queue URL
    queue_url = os.environ.get('SQS_QUEUE_URL')
    # Send a message to the SQS queue

    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageBody=message
    )

    print(response['MessageId'])
