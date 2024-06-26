'''The provided Python script accomplishes the following tasks:

1. Reads data from the "H_list.csv" file and the "mapping_ebba2.csv" file.
2. Compares the scientific names in the "H_list.csv" with the "Scientific Name" column in the "mapping_ebba2.csv."
3. If a match is found, it extracts the corresponding scientific name and saves it to a new CSV file called "list_sp_ml.csv."
4. Names not present in both files are saved to another CSV file called "H_list_dissimilar.csv."

In summary, the script performs data comparison and extraction, resulting in two separate CSV files.'''

import pandas as pd

# Read data from H_list.csv
h_list_path = r"E:\BIOACOUSTICS_PROJECT\prev_files\H_list.csv"
h_list_df = pd.read_csv(h_list_path)

# Read data from mapping_ebba2.csv
mapping_path = r"E:\BIOACOUSTICS_PROJECT\B_model_code\inputs\mapping_ebba2.csv"
mapping_df = pd.read_csv(mapping_path)

# Extract the scientific name columns
h_scientific_names = h_list_df["scientific name"]
mapping_scientific_names = mapping_df["Scientific Name"]

# Find matching scientific names
matching_scientific_names = set(h_scientific_names) & set(mapping_scientific_names)

# Create a DataFrame for matching names
matching_df = pd.DataFrame({"SP": list(matching_scientific_names)})

# Save matching names to C:\Users\newbr\OneDrive\Desktop\New folder\list_sp_ml.csv
matching_df.to_csv(r"C:\Users\newbr\OneDrive\Desktop\New folder\list_sp_ml.csv", index=False)

# Create a DataFrame for dissimilar names
dissimilar_df = h_list_df[~h_list_df["scientific name"].isin(matching_scientific_names)]

# Save dissimilar names to C:\Users\newbr\OneDrive\Desktop\New folder\H_list_dissimilar.csv
dissimilar_df.to_csv(r"C:\Users\newbr\OneDrive\Desktop\New folder\H_list_dissimilar.csv", index=False)

print("Comparison complete. Results saved to list_sp_ml.csv and H_list_dissimilar.csv")