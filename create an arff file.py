import pandas as pd
import arff
import os

# Define paths
train_csv_path = r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\enhanced_personnel_train.csv'
test_csv_path = r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\missingvalues_personnel_test.csv'

train_arff_path = r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\personnel_train.arff'
test_arff_path = r'C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\personnel_test.arff'

# Load datasets
train_df = pd.read_csv(train_csv_path)
test_df = pd.read_csv(test_csv_path)

# Function to convert DataFrame to ARFF
def convert_to_arff(df, file_path):
    # Prepare the attributes
    attributes = []
    for column in df.columns:
        if df[column].dtype == 'object':
            unique_values = df[column].unique().tolist()
            attributes.append((column, unique_values))
        elif df[column].dtype == 'int64' or df[column].dtype == 'float64':
            attributes.append((column, 'NUMERIC'))
    
    # Convert DataFrame to list of lists
    data = df.values.tolist()

    # Create ARFF dictionary
    arff_dict = {
        'description': '',
        'relation': os.path.splitext(os.path.basename(file_path))[0],
        'attributes': attributes,
        'data': data
    }

    # Write ARFF file
    with open(file_path, 'w') as f:
        arff.dump(arff_dict, f)
    print(f"ARFF file saved at {file_path}")

# Convert and save the datasets
convert_to_arff(train_df, train_arff_path)
convert_to_arff(test_df, test_arff_path)
