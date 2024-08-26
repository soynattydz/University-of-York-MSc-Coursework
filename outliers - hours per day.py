import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned datasets
train_data_path = r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\cleaned_personnel_train.csv'
test_data_path = r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\personnel_test.csv'
personnel_train_cleaned = pd.read_csv(train_data_path)
personnel_test_cleaned = pd.read_csv(test_data_path)

# Cap DailyRate and HourlyRate at reasonable values for both datasets
for df in [personnel_train_cleaned, personnel_test_cleaned]:
    df['DailyRate'] = df['DailyRate'].clip(upper=1500)
    df['HourlyRate'] = df['HourlyRate'].clip(lower=30, upper=100)

   # Adjust StockOptionLevel from 0-3 to 1-4
    df['StockOptionLevel'] = df['StockOptionLevel'] + 1

# Creating new attributes
def create_new_features(df):
    # 1. Hours Worked per Day
    df['HoursWorkedPerDay'] = df['DailyRate'] / df['HourlyRate']
    df.loc[df['HoursWorkedPerDay'] > 24, 'HoursWorkedPerDay'] = 24  # Cap unrealistic values at 24

    # 2. Monthly Income per Job Level
    df['IncomePerJobLevel'] = df['MonthlyIncome'] / df['JobLevel']

    # 3. Total Income Over Years at Company
    df['TotalIncomeOverYears'] = df['MonthlyIncome'] * 12 * df['YearsAtCompany']

    # 4. Years Since Last Promotion Ratio
    df['PromotionToYearsRatio'] = df['YearsSinceLastPromotion'] / (df['YearsAtCompany'] + 1)

    # 5. Average Tenure per Job Role
    average_tenure_per_role = df.groupby('JobRole')['YearsAtCompany'].transform('mean')
    df['AvgTenurePerJobRole'] = average_tenure_per_role

    # 6. Average Satisfaction Score
    df['AvgSatisfaction'] = df[['EnvironmentSatisfaction', 'JobSatisfaction', 'RelationshipSatisfaction']].mean(axis=1)

    # 7. Work-Life Satisfaction Composite Score
    df['WorkLifeSatisfaction'] = (df['WorkLifeBalance'] + 
                                  df['JobSatisfaction'] + 
                                  df['EnvironmentSatisfaction']) / 3

    # 8. Career Start Indicator
    df['StartedAtCompany'] = (df['TotalWorkingYears'] == df['YearsAtCompany']).astype(int)

    # 9. Proportion of Career Spent at the Company
    df['ProportionCareerAtCompany'] = df['YearsAtCompany'] / (df['TotalWorkingYears'] + 1)

    return df

# Apply the function to both datasets
personnel_train_cleaned = create_new_features(personnel_train_cleaned)
personnel_test_cleaned = create_new_features(personnel_test_cleaned)

# Save the enhanced datasets to new CSV files
enhanced_train_data_path = r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\enhanced_personnel_train.csv'
enhanced_test_data_path = r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\enhanced_personnel_test.csv'

personnel_train_cleaned.to_csv(enhanced_train_data_path, index=False)
personnel_test_cleaned.to_csv(enhanced_test_data_path, index=False)

print("New features created and datasets saved as enhanced_personnel_train.csv and enhanced_personnel_test.csv")

# Plot histograms to visualize distributions
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.histplot(personnel_train_cleaned['DailyRate'], kde=True)
plt.title('DailyRate Distribution')

plt.subplot(1, 2, 2)
sns.histplot(personnel_train_cleaned['HourlyRate'], kde=True)
plt.title('HourlyRate Distribution')

plt.show()
