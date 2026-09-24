# List containing clean display names for each category
expense_categories = ["Material Cost", "Labor Cost", "Overhead Cost"]

# Variance data for each category
variance_data = []

print("Enter the Actual and Budgeted costs for each category:\n")

# Loop to collect costs for each category
for category in expense_categories:
    actual_cost = float(input(f"Enter Actual cost for {category}: "))
    budgeted_cost = float(input(f"Enter Budgeted cost for {category}: "))
    
    # Calculate variance (Actual - Budget)
    variance = actual_cost - budgeted_cost
    
    # Mark as FAVORABLE if Actual <= Budget (variance <= 0)
    status = "FAVORABLE" if variance <= 0 else "UNFAVORABLE"
    
    # Append the completed data dictionary
    variance_data.append({
        "Category": category,
        "Actual Cost": actual_cost,
        "Budgeted Cost": budgeted_cost,
        "Variance": variance,
        "Status": status
    })

# Print the variance report
print("\n" + "=" * 35)
print("         VARIANCE REPORT         ")
print("=" * 35)

for data in variance_data:
    print(f"Category:      {data['Category']}")
    print(f"Actual Cost:   ${data['Actual Cost']:,.2f}")
    print(f"Budgeted Cost: ${data['Budgeted Cost']:,.2f}")
    print(f"Variance:      ${abs(data['Variance']):,.2f}")
    print(f"Status:        {data['Status']}")
    print("-" * 35)