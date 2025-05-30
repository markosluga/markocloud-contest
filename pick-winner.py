import boto3
from uuid import uuid4

dynamodb = boto3.resource('dynamodb')
 # Set your table name as an environment variable. You can also hardcode the table name by replacing os.environ['table'] with 'your-table-name' here if you like.
tableName = dynamodb.Table(os.environ['table'])

def lambda_handler(event, context):
    # This code sets a limit of 1000 records. Please adjust these to your desired size.
    for i in range(1):
        response = table.scan(
            Limit=1000,
        )
        # Define contestants as number of items in the response 
        contestants = len(response['Items'])
        # Print the number of contestants
        print("Number of contestants: ", contestants)
        # Pick a random number between 1 and the number of contestants
        winner = uuid4().int % contestants
        # Select the dynamodb item at the random number
        winner = response['Items'][winner]
        # Print the winner
        print("Winner: ", winner)
