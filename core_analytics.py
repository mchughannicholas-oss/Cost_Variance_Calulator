# List containing clean display names for each category
expense_categories = ["Material Cost", "Labor Cost", "Overhead Cost"]

# Calculate variance (Actual - Budget)
def calculate_variance(actual_cost, budgeted_cost):
    variance = actual_cost - budgeted_cost
    return variance

# Determine status based on variance
def determine_status(variance):
    status = "FAVORABLE" if variance <= 0 else "UNFAVORABLE"
    return status

def process_all_categories(categories, actual_costs, budgeted_costs):
    """Loops through categories, calculates variances, and returns a list of dictionaries."""
    variance_data = []

    for category, actual_cost, budgeted_cost in zip(categories, actual_costs, budgeted_costs):
        variance = calculate_variance(actual_cost, budgeted_cost)
        status = determine_status(variance)    
        
        # Append the completed data dictionary INSIDE the loop
        variance_data.append({
            "Category": category,
            "Actual Cost": actual_cost,
            "Budgeted Cost": budgeted_cost,
            "Variance": variance,
            "Status": status
        })
        
    return variance_data
