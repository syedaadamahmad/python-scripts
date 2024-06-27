import pandas as pd

# Read data from list_sp_ml.csv
list_sp_ml_path = r"C:\Users\newbr\OneDrive\Desktop\New folder\list_sp_ml.csv"
list_sp_ml_df = pd.read_csv(list_sp_ml_path)

# Read data from mapping_ebba.csv
mapping_path = r"E:\BIOACOUSTICS_PROJECT\B_model_code\inputs\mapping_ebba2.csv"
mapping_df = pd.read_csv(mapping_path)

# Create a dictionary to map scientific names to English Name Variant 2
name_mapping = dict(zip(mapping_df["Scientific Name"], mapping_df["English Name Variant 2"]))

# Initialize an empty list to store English names in the correct order
english_names_ordered = []

# Iterate through the scientific names in list_sp_ml.csv
for scientific_name in list_sp_ml_df["SP"]:
    english_name = name_mapping.get(scientific_name, "")  # Get the corresponding English name
    english_names_ordered.append(english_name)

# Create a DataFrame with the ordered English names
ordered_df = pd.DataFrame({"English Name Variant 2": english_names_ordered})

# Save ordered names to list_en_ml.csv
ordered_df.to_csv(r"C:\Users\newbr\OneDrive\Desktop\New folder\list_en_ml.csv", index=False)

print("Comparison complete. Ordered results saved to list_en_ml.csv")