import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:/Users/natal/OneDrive/University of York - CS and AI/BDA/BDA Reassessment 23-24 Dataset/enhanced_personnel_train.csv')

# Separate the data based on Attrition
attrition_yes = df[df['Attrition'] == 'Yes']
attrition_no = df[df['Attrition'] == 'No']

# Save the separate datasets to CSV files
attrition_yes.to_csv(r'C:/Users/natal/OneDrive/University of York - CS and AI/BDA/BDA Reassessment 23-24 Dataset/attrition_yes.csv', index=False)
attrition_no.to_csv(r'C:/Users/natal/OneDrive/University of York - CS and AI/BDA/BDA Reassessment 23-24 Dataset/attrition_no.csv', index=False)

print('Datasets have been separated and saved as attrition_yes.csv and attrition_no.csv.')
