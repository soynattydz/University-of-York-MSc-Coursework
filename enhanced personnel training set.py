import pandas as pd

# Load the cleaned dataset
train_data_path = r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\cleaned_personnel_train.csv'
personnel_train_cleaned = pd.read_csv(train_data_path)

# Creating new attributes
# 1. Hours Worked per Day
personnel_train_cleaned['HoursWorkedPerDay'] = personnel_train_cleaned['DailyRate'] / personnel_train_cleaned['HourlyRate']

# 2. Monthly Income per Job Level
personnel_train_cleaned['IncomePerJobLevel'] = personnel_train_cleaned['MonthlyIncome'] / personnel_train_cleaned['JobLevel']

# 3. Total Income Over Years at Company
personnel_train_cleaned['TotalIncomeOverYears'] = personnel_train_cleaned['MonthlyIncome'] * 12 * personnel_train_cleaned['YearsAtCompany']

# 4. Years Since Last Promotion Ratio
personnel_train_cleaned['PromotionToYearsRatio'] = personnel_train_cleaned['YearsSinceLastPromotion'] / (personnel_train_cleaned['YearsAtCompany'] + 1)

# 5. Average Tenure per Job Role
average_tenure_per_role = personnel_train_cleaned.groupby('JobRole')['YearsAtCompany'].transform('mean')
personnel_train_cleaned['AvgTenurePerJobRole'] = average_tenure_per_role

# 6. Average Satisfaction Score
personnel_train_cleaned['AvgSatisfaction'] = personnel_train_cleaned[['EnvironmentSatisfaction', 'JobSatisfaction', 'RelationshipSatisfaction']].mean(axis=1)

# 7. Work-Life Satisfaction Composite Score
personnel_train_cleaned['WorkLifeSatisfaction'] = (personnel_train_cleaned['WorkLifeBalance'] + 
                                                   personnel_train_cleaned['JobSatisfaction'] + 
                                                   personnel_train_cleaned['EnvironmentSatisfaction']) / 3

# 9. Career Start Indicator
personnel_train_cleaned['StartedAtCompany'] = (personnel_train_cleaned['TotalWorkingYears'] == personnel_train_cleaned['YearsAtCompany']).astype(int)

# 10. Proportion of Career Spent at the Company
personnel_train_cleaned['ProportionCareerAtCompany'] = personnel_train_cleaned['YearsAtCompany'] / (personnel_train_cleaned['TotalWorkingYears'] + 1)

# Save the enhanced dataset to a new CSV file
enhanced_data_path = r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\enhanced_personnel_train.csv'
personnel_train_cleaned.to_csv(enhanced_data_path, index=False)

print("New features created and dataset saved as enhanced_personnel_train.csv")
