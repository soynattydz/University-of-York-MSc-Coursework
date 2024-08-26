import pandas as pd

def csv_to_arff(csv_file_path, arff_file_path, relation_name):
    df = pd.read_csv(csv_file_path)

    with open(arff_file_path, 'w') as f:
        # Write the relation name
        f.write(f"@relation {relation_name}\n\n")
        
        # Write the attributes
        for col in df.columns:
            if df[col].dtype == 'object':
                unique_vals = df[col].unique()
                f.write(f"@attribute {col} {{{','.join(map(str, unique_vals))}}}\n")
            else:
                f.write(f"@attribute {col} numeric\n")
        
        # Write the data
        f.write("\n@data\n")
        for index, row in df.iterrows():
            row_str = ','.join(map(str, row))
            f.write(f"{row_str}\n")

    print(f"ARFF file saved at {arff_file_path}")

# File paths
csv_file_paths = [
    r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\attrition_yes.csv',
    r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\attrition_no.csv'
]
arff_file_paths = [
    r'C:/Users/natal/OneDrive/University of York - CS and AI/BDA/BDA Reassessment 23-24 Dataset/ATTRITION_YES_trainingset.arff',
    r'C:/Users/natal/OneDrive/University of York - CS and AI/BDA/BDA Reassessment 23-24 Dataset/ATTRITION_NO_trainingset.arff'
]
relation_names = ['ATTRITION_YES_trainingset', 'ATTRITION_NO_trainingset']

# Convert CSV files to ARFF
for csv_file, arff_file, relation_name in zip(csv_file_paths, arff_file_paths, relation_names):
    csv_to_arff(csv_file, arff_file, relation_name)
