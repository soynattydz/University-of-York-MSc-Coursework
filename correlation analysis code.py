# Perform correlation analysis
correlation_matrix = personnel_train_cleaned[['JobLevel', 'Age', 'MonthlyIncome', 'DistanceFromHome', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']].corr()

# Display correlation matrix
print("\nCorrelation Matrix:")
print(correlation_matrix)