"""
app.py- VisitorCounterFunction

Provides functionality to my portfolio web application's 'visitor counter' by communicating between AWS API Gateway and AWS DynamoDB. 

This function is intended to be deployed to AWS Lambda in a SAM Template for use in my Portfolio Backend Stack.
"""

import json
import os
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ["TABLE_NAME"])

def lambda_handler(event, context):
    """
    Provides backend API functionality for my portfolio web application.

    Receives HTTP requests from AWS API Gateway which are triggers to increment a persistent visitor count in AWS DynamoDB.
    This final number from DynamoDB is then returned to the web application for display.

    Args:
        event(dict): AWS API Gateway package containing request metadata. This function does not rely on this parameter, the function invocation itself counts as a visit.
        context: Runtime information provided by AWS Lambda. Not utilized by this function.
        
    Returns:
        JSON response(200): Returned if the DynamoDB table is successfully incremented, and a value is returned from the table to be sent to the web application.
        JSON response(500): Returned if the DynamoDB table incrementing fails for any reason.

    Raises:
        ClientError: Raised if there are any errors that occur during the course of the function.
    """
    try:
        response = table.update_item(
            Key={
                "id": "visitors"
            },
            UpdateExpression="ADD visit_count :inc",
            ExpressionAttributeValues={
                ":inc": 1
            },
            ReturnValues="UPDATED_NEW"
        )

        count = int(response["Attributes"]["visit_count"])

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": ["https://zacaryharmon.com", "https://www.zacaryharmon.com"],
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "count": count
            })}
    except ClientError as e:
        print("DynamoDB error:", e)

        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": ["https://zacaryharmon.com", "https://www.zacaryharmon.com"],
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Failed to update counter"
            })}
        
