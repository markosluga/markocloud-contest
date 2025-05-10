import pandas as pd

# Load the CSV file
# In the line below, change the CSVsample name to the name of your csv file
df = pd.read_csv('CSVsample.csv', encoding='cp1252')

# Define the number of records per split
chunk_size = 25

# Split the DataFrame into chunks
for i in range(0, len(df), chunk_size):
    chunk = df.iloc[i:i + chunk_size]
    # In the line below, change the CSVsample name to the name of your csv file
    chunk.to_csv(f'CSVsample{i // chunk_size + 1}.csv', index=False)
