import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the cleaned dataset
train_data_path = r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\cleaned_personnel_train.csv'
personnel_train_cleaned = pd.read_csv(train_data_path)

# Perform correlation analysis
correlation_matrix = personnel_train_cleaned[['JobLevel', 'Age', 'MonthlyIncome', 'DistanceFromHome', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']].corr()

# Display correlation matrix
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Plot correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# Plot distribution of some key attributes
plt.figure(figsize=(15, 10))

# Age distribution
plt.subplot(2, 2, 1)
sns.histplot(personnel_train_cleaned['Age'], kde=True, bins=30)
plt.title('Age Distribution')

# Monthly Income distribution
plt.subplot(2, 2, 2)
sns.histplot(personnel_train_cleaned['MonthlyIncome'], kde=True, bins=30)
plt.title('Monthly Income Distribution')

# Distance From Home distribution
plt.subplot(2, 2, 3)
sns.histplot(personnel_train_cleaned['DistanceFromHome'], kde=True, bins=30)
plt.title('Distance From Home Distribution')

# Years At Company distribution
plt.subplot(2, 2, 4)
sns.histplot(personnel_train_cleaned['YearsAtCompany'], kde=True, bins=30)
plt.title('Years At Company Distribution')

plt.tight_layout()
plt.show()
