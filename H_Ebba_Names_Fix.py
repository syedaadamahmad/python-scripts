'''The provided Python script performs the following tasks:

1. Reads data from the "H_list_dissimilar.csv" file.
2. Reads data from the "mapping_ebba.csv" file.
3. Compares the names in the "Common name" column of "H_list_dissimilar.csv" with the names in the "English Name Variant 1" column of "mapping_ebba.csv."
4. If a name is present in both columns, it extracts the corresponding scientific name (from the first column of "mapping_ebba.csv").
5. Saves the matching scientific names to a new CSV file called "list_sp_ml_more.csv."
6. Names not present in both columns are saved to another list called "H_list_dissimilar_rem.csv."

The script effectively processes and compares data between the two CSV files.'''


import pandas as pd

# Read data from H_list_dissimilar.csv
h_dissimilar_path = r"C:\Users\newbr\OneDrive\Desktop\New folder\H_list_dissimilar.csv"
h_dissimilar_df = pd.read_csv(h_dissimilar_path)

# Read data from mapping_ebba.csv
mapping_path = r"E:\BIOACOUSTICS_PROJECT\B_model_code\inputs\mapping_ebba2.csv"
mapping_df = pd.read_csv(mapping_path)

# Extract Common name and English Name Variant 1 columns
common_names = h_dissimilar_df["Common name"]
english_names = mapping_df["English Name Variant 1"]
scientific_names = mapping_df["Scientific Name"]

# Find matching names
matching_indices = h_dissimilar_df.index[h_dissimilar_df["Common name"].isin(english_names)]

# Create a DataFrame for matching names
matching_df = pd.DataFrame({"SP": scientific_names.loc[matching_indices]})

# Save matching names to list_sp_ml_more.csv
matching_df.to_csv(r"C:\Users\newbr\OneDrive\Desktop\New folder\list_sp_ml_more.csv", index=False)

# Create a DataFrame for dissimilar names
dissimilar_rem_df = h_dissimilar_df.loc[~h_dissimilar_df.index.isin(matching_indices)]

# Save dissimilar names to H_list_dissimilar_rem.csv
dissimilar_rem_df.to_csv(r"C:\Users\newbr\OneDrive\Desktop\New folder\H_list_dissimilar_rem.csv", index=False)

print("Comparison complete. Results saved to list_sp_ml_more.csv and H_list_dissimilar_rem.csv")