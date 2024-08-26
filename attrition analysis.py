import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
train_data_path = r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\cleaned_personnel_train.csv'
personnel_train_cleaned = pd.read_csv(train_data_path)

# List of potential key attributes
key_attributes = ['Age', 'Department', 'JobRole', 'MonthlyIncome', 'OverTime', 'JobLevel', 'DistanceFromHome', 'YearsAtCompany']

# Plot the distribution of key attributes by Attrition
for attribute in key_attributes:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=personnel_train_cleaned, x=attribute, hue='Attrition')
    plt.title(f'Distribution of {attribute} by Attrition')
    plt.xticks(rotation=45)
    plt.show()

# Calculate mean averages for relevant attributes
remaining = personnel_train_cleaned[personnel_train_cleaned['Attrition'] == 'No']
leaving = personnel_train_cleaned[personnel_train_cleaned['Attrition'] == 'Yes']

mean_remaining = remaining.mean()
mean_leaving = leaving.mean()

print("Mean Averages of Staff Remaining:")
print(mean_remaining)

print("Mean Averages of Staff Leaving:")
print(mean_leaving)
