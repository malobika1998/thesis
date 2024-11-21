import pandas as pd
from textblob import TextBlob
import re

# Load the data from your CSV file
data = pd.read_csv('filtered_covid19_data.csv')

# Display the columns to verify
print(data.columns)

# Define a function to clean the text
def clean_text(text):
    text = str(text).lower()  # Convert text to lowercase
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

# Apply the cleaning function to the 'THEMES' column
data['themes_clean'] = data['THEMES'].apply(clean_text)

# Define a function for sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Returns sentiment polarity

# Apply sentiment analysis to the 'themes_clean' column
data['sentiment'] = data['themes_clean'].apply(analyze_sentiment)

# Display the result: Date, Themes, and Sentiment
print(data[['DATE', 'THEMES', 'sentiment']].head())

# Optionally, save the processed data to a new CSV
data.to_csv('processed_data.csv', index=False)

