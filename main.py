import core_analytics
import streamlit as st

#Title and description for the Streamlit app
st.title("📊 Financial Cost Variance Calculator")
st.markdown("Compare your budgeted expenses against actual costs.")

# Create input fields for each category so the user can type actual and budgeted costs
actual_costs = []
budgeted_costs = []

st.subheader("Enter Actual and Budgeted Costs for Each Category")

# List containing clean display names for each category
expense_categories = ["Material Cost", "Labor Cost", "Overhead Cost"]

# Loop through your categories from core.py to create inputs dynamically
for category in expense_categories:
    st.markdown(f"**{category}**")
    col1, col2 = st.columns(2)
    with col1:
        act = st.number_input(f"Actual {category}", min_value=0.0, value=0.0, key=f"act_{category}")
    with col2:
        bud = st.number_input(f"Budgeted {category}", min_value=0.0, value=0.0, key=f"bud_{category}")
    
    actual_costs.append(act)
    budgeted_costs.append(bud)

# When the user clicks the "Calculate Variance" button, perform the calculations
if st.button("Calculate Variance", key="calc_variance_btn"):
    results = core_analytics.process_all_categories(expense_categories, actual_costs, budgeted_costs)

    st.success("Variance calculation completed successfully!")

    # Display the variance report in the Streamlit app
    st.subheader("Variance Report")
    
    # The full ledger table
    st.dataframe(results, use_container_width=True)   
    