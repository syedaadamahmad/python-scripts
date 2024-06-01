import os
import pandas as pd

# Specify the paths to relevant files
subfolder_dir = r'C:\Users\newbr\OneDrive\Desktop\BIOACOUSTICS_PROJECT\B_model_code\all_audio_split_temp'
mapping_csv_path = r'C:\Users\newbr\OneDrive\Desktop\BIOACOUSTICS_PROJECT\B_model_code\inputs\mapping_ebba2.csv'
output_en_csv_path = r'C:\Users\newbr\OneDrive\Desktop\BIOACOUSTICS_PROJECT\B_model_code\inputs\list_en_ml_0.csv'
output_sp_csv_path = r'C:\Users\newbr\OneDrive\Desktop\BIOACOUSTICS_PROJECT\B_model_code\inputs\list_sp_ml_0.csv'

# Step 1: Extract subfolder names
subfolder_names = [folder for folder in os.listdir(subfolder_dir) if os.path.isdir(os.path.join(subfolder_dir, folder))]

# Read the mapping CSV file
mapping_df = pd.read_csv(mapping_csv_path)

# Filter rows where "English Name Variant 2" matches subfolder names
matching_rows = mapping_df[mapping_df['English Name Variant 2'].isin(subfolder_names)]

# Save only the "English Name Variant 2" column to list_en_ml_0.csv
matching_rows[['English Name Variant 2']].to_csv(output_en_csv_path, index=False)
print(f"Saved {len(matching_rows)} English names to {output_en_csv_path}")

# Step 2: Retrieve scientific names
# Read the previously saved CSV file
en_df = pd.read_csv(output_en_csv_path)

# Merge with the mapping CSV to get scientific names
sp_df = pd.merge(en_df, mapping_df, left_on='English Name Variant 2', right_on='English Name Variant 2', how='left')

# Save only the "Scientific Name" column to list_sp_ml_0.csv
sp_df[['Scientific Name']].to_csv(output_sp_csv_path, index=False)
print(f"Saved {len(sp_df)} scientific names to {output_sp_csv_path}")