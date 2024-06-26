'''The provided Python script accomplishes the following tasks:

1. Reads data from the "list_sp_ml.csv" file, which contains scientific names.
2. Reads data from the "mapping_ebba2.csv" file.
3. Compares the scientific names from the "list_sp_ml.csv" with the "Scientific Name" column in the "mapping_ebba2.csv."
4. If a match is found, it extracts the corresponding English Name Variant 2 (from the fourth column of "mapping_ebba2.csv").
5. Saves the matching English Name Variant 2 data to a new CSV file called "list_en_ml.csv."

In summary, the script identifies related English names for the given scientific names and creates a separate CSV file with the extracted information.'''

import pandas as pd

# Read data from list_sp_ml.csv
list_sp_ml_path = r"C:\Users\newbr\OneDrive\Desktop\New folder\list_sp_ml.csv"
list_sp_ml_df = pd.read_csv(list_sp_ml_path)

# Read data from mapping_ebba.csv
mapping_path = r"E:\BIOACOUSTICS_PROJECT\B_model_code\inputs\mapping_ebba2.csv"
mapping_df = pd.read_csv(mapping_path)

# Extract SP and Scientific Name columns
sp_names = list_sp_ml_df["SP"]
scientific_names = mapping_df["Scientific Name"]

# Find matching scientific names
matching_indices = list_sp_ml_df.index[list_sp_ml_df["SP"].isin(scientific_names)]

# Create a DataFrame for matching names
matching_df = pd.DataFrame({"English Name Variant 2": mapping_df["English Name Variant 2"].loc[matching_indices]})

# Save matching names to list_en_ml.csv
matching_df.to_csv(r"C:\Users\newbr\OneDrive\Desktop\New folder\list_en_ml.csv", index=False)

print("Comparison complete. Results saved to list_en_ml.csv")