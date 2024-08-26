import pandas as pd

# Load the datasets
attrition_no = pd.read_csv(r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\attrition_no.csv')
attrition_yes = pd.read_csv(r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\attrition_yes.csv')

# Calculate percentages
total_count = len(attrition_no) + len(attrition_yes)
percent_no = (len(attrition_no) / total_count) * 100
percent_yes = (len(attrition_yes) / total_count) * 100

# Calculate mean averages
mean_no = attrition_no.mean()
mean_yes = attrition_yes.mean()

# Print results
print("Percentages:")
print(f"Attrition=No: {percent_no:.2f}%")
print(f"Attrition=Yes: {percent_yes:.2f}%\n")

print("Mean Averages for Attrition=No:")
print(mean_no)

print("\nMean Averages for Attrition=Yes:")
print(mean_yes)
