"""
ticket_dashboard.py
Author: AZ
Date: April 2025

This script simulates IT consulting work by analyzing a support ticket dataset.
It summarizes resolution speed, team load, and ticket types using pandas.
"""

import pandas as pd

# Simulated ticket data
data = pd.DataFrame({
    "Ticket ID": [101, 102, 103, 104, 105, 106, 107],
    "Technician": ["Sam", "Alex", "Sam", "Dana", "Alex", "Sam", "Dana"],
    "Issue Type": ["Network", "Login", "Network", "Software", "Login", "Hardware", "Hardware"],
    "Status": ["Closed", "Closed", "Open", "Closed", "Open", "Closed", "Closed"],
    "Resolution Time (hrs)": [5, 2, None, 4, None, 3, 6]
})

# Fill missing resolution time with 0 for open tickets
data["Resolution Time (hrs)"] = data["Resolution Time (hrs)"].fillna(0)

# Total tickets per technician
tech_summary = data["Technician"].value_counts()

# Average resolution time
avg_resolution = data["Resolution Time (hrs)"].mean()

# Open vs closed ratio
status_counts = data["Status"].value_counts()

# Top 3 issue types
top_issues = data["Issue Type"].value_counts().head(3)

# Output
print("📊 Ticket Dashboard")
print("-------------------------")
print(f"Average Resolution Time: {avg_resolution:.2f} hrs\n")

print("Tickets per Technician:")
print(tech_summary, "\n")

print("Ticket Status Breakdown:")
print(status_counts, "\n")

print("Top 3 Issue Types:")
print(top_issues)
