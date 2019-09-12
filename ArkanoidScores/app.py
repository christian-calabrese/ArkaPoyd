import sys
import boto3
import json
from chalice import Chalice
from boto3.dynamodb.conditions import Key

client = boto3.client('dynamodb')
app = Chalice(app_name='ArkanoidScores')

@app.route('/score')
def get_highest():
    response = client.query(
        TableName = 'ArkanoidScores',
        Limit = 1,
        ScanIndexForward = False
    )
    json_resp = json.dumps(response.get("Items"))
    return json_resp

@app.route('/score', methods=['POST'])
def push_score():
    parsed = json.loads(app.current_request._body)

    client.put_item(
        TableName='ArkanoidScores',
        Item={
            'score':
            {
                'S': parsed.get('score'),
            },
            'name':
            {
                'S': 'XXX',
            }
        }
    )