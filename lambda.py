import json
import os
import mercadopago

def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN"])
    data =json.loads(event["body"])

    payment_response = sdk.payment().create(data)
    json_data ={
        "status": payment_response["response"]["status"],
        "status_detail": payment_response["response"]["status_detail"],
        "id": payment_response["response"]["id"]
    }
    
    return {
        "statusCode": 201,
        # "body": json.dumps(json_data),
        "body": json.dumps(payment_response["response"])
    }
    