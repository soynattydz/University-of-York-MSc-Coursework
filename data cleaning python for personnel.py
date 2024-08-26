import pandas as pd

# Load datasets
test_data_path = r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\enhanced_personnel_test.csv'
personnel_test = pd.read_csv(test_data_path)

# Replace missing values with ?
personnel_test = personnel_test.replace({pd.NA: '?'})
personnel_test = personnel_test.replace({pd.NaT: '?'})
personnel_test = personnel_test.replace({float('nan'): '?'})

# Replace NumCompaniesWorked values of 0 with 1
personnel_test['NumCompaniesWorked'] = personnel_test['NumCompaniesWorked'].replace(0, 1)

# Remove irrelevant columns
columns_to_remove = ['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours']
personnel_test.drop(columns=columns_to_remove, inplace=True)

# Save the cleaned data to a new CSV file
output_path = r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\missingvalues_personnel_test.csv'
personnel_test.to_csv(output_path, index=False)

# Display the first few rows of the cleaned test dataset to confirm changes
print(personnel_test.head())
