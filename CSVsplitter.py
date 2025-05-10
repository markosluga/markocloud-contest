import pandas as pd

# Load the CSV file
df = pd.read_csv('contest.csv', encoding='cp1252')

# Define the number of records per split
chunk_size = 25

# Split the DataFrame into chunks
for i in range(0, len(df), chunk_size):
    chunk = df.iloc[i:i + chunk_size]
    chunk.to_csv(f'contest{i // chunk_size + 1}.csv', index=False)
