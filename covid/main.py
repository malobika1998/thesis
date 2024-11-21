

import pandas as pd

# Step 1: Load the GDELT CSV file (replace with the correct file path)
file_path = 'C:/Users/Dell/Desktop/Thesis/20191201.gkg.csv'  # Update with your actual file path
data = pd.read_csv(file_path, sep="\t", encoding='latin-1')

# Step 2: Inspect the column names to ensure 'THEMES' column exists
print("Column Names:")
print(data.columns)

# Step 3: Strip any extra spaces from column names to avoid KeyError
data.columns = data.columns.str.strip()

# Step 4: Display the first few rows to understand the structure of the dataset
print("\nFirst few rows of the data:")
print(data.head())

# Step 5: Check if 'THEMES' column exists and then filter rows for the desired keywords
if 'THEMES' in data.columns:
    # Define the keywords related to COVID-19
    keywords = ["COVID-19", "CORONAVIRUS", "PANDEMIC", "VIRUS", "COVID"]

    # Filter the rows where 'THEMES' contains any of the keywords
    filtered_data = data[data['THEMES'].str.contains('|'.join(keywords), na=False, case=False)]

    # Display the filtered data
    print("\nFiltered Data:")
    print(filtered_data.head())

    # Step 6: Save the filtered data to a new CSV file
    filtered_data.to_csv('filtered_covid19_data.csv', index=False)
    print("\nFiltered data saved to 'filtered_covid19_data.csv'")
    
    # Step 7: Extract and save URLs from the 'SOURCEURLS' column (if needed)
    urls = filtered_data['SOURCEURLS']
    urls.to_csv('filtered_covid19_urls.txt', index=False, header=False)
    print("\nFiltered URLs saved to 'filtered_covid19_urls.txt'")
else:
    print("\nError: 'THEMES' column not found. Please check the dataset structure.")


