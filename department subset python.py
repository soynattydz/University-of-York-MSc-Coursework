import pandas as pd
import subprocess

# Load the dataset
df = pd.read_csv(r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\missingvalues_personnel_test.csv')

# Split by department and save each subset as a CSV
departments = df['Department'].unique()
for dept in departments:
    subset = df[df['Department'] == dept]
    csv_file = f'dataset_{dept}.csv'
    arff_file = f'dataset_{dept}.arff'
    
    # Save as CSV
    subset.to_csv(csv_file, index=False)

    # Convert to ARFF using Weka's CSVLoader
    subprocess.run(['java', '-cp', 'C:/Program Files/Weka-3-8-6/weka.jar', 'weka.core.converters.CSVLoader', csv_file, '-o', arff_file])
