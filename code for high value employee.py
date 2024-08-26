import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\enhanced_personnel_train.csv')

# Calculate the mean values for the specified columns
mean_job_level = df['JobLevel'].mean()
mean_monthly_income = df['MonthlyIncome'].mean()
mean_daily_rate = df['DailyRate'].mean()
mean_performance_rating = df['PerformanceRating'].mean()
mean_promotion_to_years_ratio = df['PromotionToYearsRatio'].mean()

# Define criteria for high-value employees
high_value_criteria = (
    (df['JobLevel'] > mean_job_level) &
    (df['MonthlyIncome'] > mean_monthly_income) &
    (df['PerformanceRating'] > mean_performance_rating)
)

# Filter the dataset
high_value_employees = df[high_value_criteria]

# Save the high-value employees dataset
high_value_employees.to_csv('high_value_employees.csv', index=False)

print("High-value employees dataset created with {} records.".format(len(high_value_employees)))
