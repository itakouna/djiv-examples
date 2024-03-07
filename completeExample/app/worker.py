from db import update_record_status
import boto3
import os 
import time 

def process_message():
    return
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

    while True:
        # Receive messages from the queue
        response = sqs.receive_message(
            QueueUrl=queue_url,
            AttributeNames=['All'],
            MaxNumberOfMessages=1,
            WaitTimeSeconds=20
        )

        # Check if messages were received
        if 'Messages' in response:
            for message in response['Messages']:
                # Process the message
                message_id = message['id']
                time.sleep(10)
                update_record_status(message_id)

                # Delete the processed message from the queue
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=message['ReceiptHandle']
                )
        else:
            print("No messages in the queue.")

process_message()
