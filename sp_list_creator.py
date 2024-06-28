import pandas as pd

# Read the list_en_ml.csv file
list_en_ml_path = r"C:\Users\newbr\OneDrive\Desktop\B_model_89\new splits\list_en_ml.csv"
list_en_ml_df = pd.read_csv(list_en_ml_path)

# Read the mapping_ebba2.csv file
mapping_ebba2_path = r"C:\Users\newbr\OneDrive\Desktop\B_model_89\inputs\mapping_ebba2.csv"
mapping_ebba2_df = pd.read_csv(mapping_ebba2_path)

# Create a dictionary to map English names to scientific names
english_to_scientific = dict(zip(mapping_ebba2_df["English Name Variant 2"], mapping_ebba2_df["Scientific Name"]))

# Map English names in list_en_ml to scientific names
list_en_ml_df["Scientific Name"] = list_en_ml_df["subfolder_name"].map(english_to_scientific)

# Save the results to list_sp_ml.csv
list_sp_ml_path = r"C:\Users\newbr\OneDrive\Desktop\B_model_89\new splits\list_sp_ml.csv"
list_en_ml_df.to_csv(list_sp_ml_path, index=False)

print(f"Results saved to {list_sp_ml_path}")