import pandas as pd

# Load the cleaned dataset
train_data_path = r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\cleaned_personnel_train.csv'
personnel_train_cleaned = pd.read_csv(train_data_path)

# Calculate staff turnover rates
attrition_counts = personnel_train_cleaned['Attrition'].value_counts(normalize=True) * 100

# Display turnover rates
print("Staff Turnover Rates:")
print(attrition_counts)

# Perform correlation analysis
correlation_matrix = personnel_train_cleaned[['JobLevel', 'Age', 'MonthlyIncome', 'DistanceFromHome', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']].corr()

# Display correlation matrix
print("\nCorrelation Matrix:")
print(correlation_matrix)