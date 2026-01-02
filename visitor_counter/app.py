import json
import os
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ["TABLE_NAME"])

def lambda_handler(event, context):
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
                "Access-Control-Allow-Origin": "https://zacaryharmon.com",
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
                "Access-Control-Allow-Origin": "https://zacaryharmon.com",
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Failed to update counter"
            })}
        
