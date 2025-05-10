# MarkoCloud Contest

A simple solution for managing online contests using AWS services. This project provides tools to collect participant data, store it in DynamoDB, and randomly select winners.

## Overview

The MarkoCloud Contest toolkit consists of several components:

1. **CSV to DynamoDB Uploader**: AWS Lambda function to automatically upload CSV files from S3 to DynamoDB
2. **CSV Splitter**: Utility to split large CSV files into smaller chunks for easier processing
3. **Winner Picker**: AWS Lambda function to randomly select a winner from the DynamoDB table
4. CSVsamples: Provide sample format of full file and 3 exampkles of split files
5. IAM Policy JSON: Provide sample policies to be used with the CSV2DynamoDB and pick-winner lambda functions

## Components

### CSV2DynamoDB.py

AWS Lambda function that:
- Triggers when a CSV file is uploaded to an S3 bucket
- Reads the CSV file and uploads its contents to a DynamoDB table
- Processes data in batches to handle large files efficiently

#### Environment Variables:
- `table`: The name of your DynamoDB table

### CSVsplitter.py

Utility script that:
- Splits large CSV files into smaller chunks (default: 25 records per file)
- Useful for testing or when dealing with large datasets

#### Usage:
1. Update the input file name in the script (default: 'CSVsample.csv')
2. Run the script: `python CSVsplitter.py`
3. Output files will be named with sequential numbers (e.g., CSVsample1.csv, CSVsample2.csv)

### pick-winner.py

AWS Lambda function that:
- Scans the DynamoDB table to get all contestants
- Randomly selects a winner using UUID-based randomization
- Prints the winner's information

#### Configuration:
- Update the table name in the script to match your DynamoDB table
- Adjust the scan limit (default: 1000) based on your contest size

## Sample Data

The repository includes sample CSV files:
- `CSVsample.csv`: Main sample file with contestant data
- `CSVsample1.csv`, `CSVsample2.csv`, etc.: Split samples for testing

## Setup Instructions

### Prerequisites
- AWS account with appropriate permissions
- AWS CLI configured with your credentials
- Python 3.x with pandas library installed

### CSV file prep
1. Name the fist column uuid and fill it up with intigers from 1 to number of contestants. See samples provided for what the file needs to look like
2. Add the contestants in the second column. The sample file calls it 'UserName' but the colum name doesn't matter
3. Use the CSVsplitter.py to create your batch import files. The BatchWrite API call is limited to 25 items, this is why we split the main file

### DynamoDB Setup
1. Create a DynamoDB table with appropriate primary key of 'uuid'
2. Note the table name for use in the Lambda functions

### Lambda Function Setup
1. Create Lambda functions from CSV2DynamoDB.py and pick-winner.py
2. Set the environment variable key=table value=yourtablename for both the CSV2DynamoDB.py and pick-winner.py. YOu can also hardcode the table name into both, inspect the code comments to see how

### S3 Setup 
1. Create an S3 bucket
2. Configure an S3 trigger and select the CSV2DynamoDB lambda functiuon as a notification target so that the lambda can process all uploaded .csv files. Leave the prefix empty (process all uploaded files) and set the suffix to .csv so that you don't send other file types to the lambda
3. Upload test files to your S3 bucket. If the trigger has been set correctly, this should invoke the CSV2DynamoDB function and populate the DyanmoDB table. You can now check the table in the console and view the items to validate that it is populated
4. Run a test with an empty event on the pick-winner function to select a random winner. The output will be in the test data and you should be able to see both the number of contestants and a randomly selected winner in the outputs.

## Best Practices

- For large contests, consider implementing pagination in the pick-winner function (not implemented)
- Secure your AWS resources with IAM policies that have least privilege (see provided samples where you need to change 123456789000 to your account number and the us-west-2 to your region)
- Ensure you comply with all laws and regulatrions that govern your contestant data

## License

This software is offered without any guarantee or liability. While the author did not intend for this code to cause any issues, using this code is strictly your responsibility and should be done at your own risk.

## Author

MarkoCloud
