import json

def lambda_handler(event, context):
    body = "Hello, This is Sri Naga Charan Gampala graduating from Data Science at University at Buffalo and i am so much intrested in being a part of AWS team."
    statusCode = 200
    return {
        'statusCode': statusCode,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": "application/json"
        }
    }


