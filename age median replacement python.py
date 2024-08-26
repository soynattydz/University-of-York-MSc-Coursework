import pandas as pd

# Load the datasets
train_data_path = '"C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\personnel_train.csv"'
personnel_train = pd.read_csv(train_data_path)

# Define the columns to be imputed
numerical_columns_to_impute = ['Age', 'DailyRate', 'DistanceFromHome', 'NumCompaniesWorked']
categorical_columns_to_impute = ['BusinessTravel', 'MaritalStatus']

# Define the function to impute missing values
def impute_missing_values(df):
    # Replace missing values for numerical columns with the median
    for column in numerical_columns_to_impute:
        df[column].fillna(df[column].median(), inplace=True)
    
    # Replace missing values for categorical columns with the mode
    for column in categorical_columns_to_impute:
        df[column].fillna(df[column].mode()[0], inplace=True)
    
    return df

# Apply the function to the training dataset
personnel_train_cleaned = impute_missing_values(personnel_train)

# Save the cleaned data to a new CSV file
personnel_train_cleaned.to_csv('C:\Users\natal\OneDrive\University of York - CS and AI\BDA\BDA Reassessment 23-24 Dataset\cleaned_personnel_train.csv', index=False)

# Display the first few rows of the cleaned training dataset to confirm changes
print(personnel_train_cleaned.head())
