"""
customer_summary.py
Author: AZ
Date: April 2025

This script loads customer purchase data from a CSV,
calculates total spend per customer,
and displays the top 3 spenders.
"""

import pandas as pd

# Load the CSV data
df = pd.read_csv('customers.csv')

# Group by customer and calculate total spend
summary = df.groupby('Customer')['Purchase Amount'].sum().reset_index()

# Sort descending
summary = summary.sort_values(by='Purchase Amount', ascending=False)

# Display top 3 customers
print("📊 Top 3 Customers by Total Spend:")
for i, row in summary.head(3).iterrows():
    print(f"- {row['Customer']}: ${row['Purchase Amount']}")
