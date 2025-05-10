# MarkoCloud Contest

A comprehensive solution for managing online contests using AWS services. This project provides tools to collect participant data, store it in DynamoDB, and randomly select winners.

## Overview

The MarkoCloud Contest toolkit consists of several components:

1. **CSV to DynamoDB Uploader**: AWS Lambda function to automatically upload CSV files from S3 to DynamoDB
2. **CSV Splitter**: Utility to split large CSV files into smaller chunks for easier processing
3. **Winner Picker**: AWS Lambda function to randomly select a winner from the DynamoDB table

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

### DynamoDB Setup
1. Create a DynamoDB table with appropriate primary key (e.g., 'uuid')
2. Note the table name for use in the Lambda functions

### Lambda Function Setup
1. Create Lambda functions for CSV2DynamoDB and pick-winner
2. Set the environment variable for the table name in CSV2DynamoDB
3. Configure an S3 trigger for CSV2DynamoDB to process uploaded files

### Local Testing
1. Use the CSVsplitter.py to create test files
2. Upload test files to S3 to trigger the CSV2DynamoDB function
3. Run the pick-winner function to select a random winner

## Best Practices

- Ensure your CSV files have consistent headers matching your DynamoDB table attributes
- For large contests, consider implementing pagination in the pick-winner function
- Secure your AWS resources with appropriate IAM policies
- Back up your contestant data regularly

## License

[Specify your license here]

## Author

[Your Name/Organization]