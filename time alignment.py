import pandas as pd

# Load your dataset
dataset_path = r"C:\Users\natal\OneDrive\University of York - CS and AI\AAI\AAI Summative\Edited DataSets\Combined_Child_Mortality.csv"
df = pd.read_csv(dataset_path)

# Step 1: Inspect the dataset
print("Dataset Overview:")
print(df.head())
print("\nData Types:")
print(df.dtypes)

# Ensure 'Year' is numeric (if necessary)
if 'Year' in df.columns:
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# Step 2: Sort by Country and Year in ascending order
df = df.sort_values(by=['Countries_territories_areas', 'Year'], ascending=[True, True])
print("\nDataset sorted by Country and Year:")
print(df.head())

# Step 3: Function to align years within each country
def align_years(group):
    # Get the range of years for each country
    full_range = pd.Series(range(group['Year'].min(), group['Year'].max() + 1))
    
    # Reindex the group based on this full range of years
    group = group.set_index('Year').reindex(full_range).reset_index()
    
    # Rename 'index' back to 'Year'
    group = group.rename(columns={'index': 'Year'})
    
    # Fill missing values using linear interpolation or forward/backward fill
    group = group.interpolate(method='linear')
    
    return group

# Step 4: Apply the align_years function to each group of countries
df_aligned = df.groupby('Countries_territories_areas').apply(align_years).reset_index(drop=True)

# Step 5: Verify the aligned dataset
print("\nAligned Dataset:")
print(df_aligned.head())

# Step 6: Check for remaining missing values
missing_values = df_aligned.isnull().sum()
print("\nRemaining missing values:")
print(missing_values[missing_values > 0])

# Step 7: Save the aligned dataset
output_file = r"C:\Users\natal\OneDrive\University of York - CS and AI\AAI\AAI Summative\Edited DataSets\Aligned_Combined_Child_Mortality.csv"
df_aligned.to_csv(output_file, index=False)

print("\nAligned dataset saved successfully at:", output_file)
