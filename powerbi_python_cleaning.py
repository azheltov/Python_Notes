"""
powerbi_python_cleaning.py
Author: AZ
Date: April 2025

This script is designed for use inside Power BI
 using the Python scripting feature.
It performs basic data cleaning: 
removing duplicates,
filling missing values,
and normalizing column names.
"""

import pandas as pd

# In Power BI, 'dataset' variable automatically contains the imported data
try:
    df = dataset
except NameError:
    # For local testing, simulate a sample dataset
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Alice', None],
        'Age': [25, None, 25, 30],
        'Job Title': ['Engineer', 'Designer', 'Engineer', None]
    })

# Step 1: Remove duplicate rows
df = df.drop_duplicates()

# Step 2: Fill missing values
df = df.fillna('Unknown')

# Step 3: Normalize column names to lowercase and replace spaces with underscores
df.columns = [col.lower().replace(" ", "_") for col in df.columns]

# Final output for Power BI
result = df

# (Optional) For local testing outside Power BI
print(result)
