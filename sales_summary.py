"""
sales_summary.py
Author: AZ
Date: April 2025

This script simulates business analyst tasks using Python and pandas.
It loads sales data, calculates summary stats, and outputs simple business insights.
"""

import pandas as pd

# Simulated sales data (normally this would be loaded from CSV or Excel)
data = pd.DataFrame({
    'Product': ['Widget A', 'Widget B', 'Widget A', 'Widget C', 'Widget B'],
    'Units Sold': [10, 5, 8, 3, 7],
    'Unit Price': [20, 35, 20, 40, 35]
})

# Calculate revenue
data['Revenue'] = data['Units Sold'] * data['Unit Price']

# Summary stats
total_revenue = data['Revenue'].sum()
avg_order_value = data['Revenue'].mean()
top_product = data.groupby('Product')['Revenue'].sum().idxmax()

# Output
print("📊 Business Summary:")
print("---------------------")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Order Value: ${avg_order_value:.2f}")
print(f"Top-Selling Product: {top_product}")
