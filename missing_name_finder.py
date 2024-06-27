import os
import pandas as pd

# Define paths
list_en_ml_path = r"C:\Users\newbr\OneDrive\Desktop\New folder\list_en_ml.csv"
h_list_89_path = r"D:\B_model_code\H_list_89"
missing_file_csv = r"C:\Users\newbr\OneDrive\Desktop\New folder\missing_file.csv"

# Read filenames from list_en_ml.csv
list_en_ml_df = pd.read_csv(list_en_ml_path)
list_en_ml_filenames = set(list_en_ml_df["SP"])

# Get filenames in H_list_89
h_list_89_filenames = set(os.listdir(h_list_89_path))

# Find missing filenames
missing_filenames = list_en_ml_filenames - h_list_89_filenames

# Create DataFrame for missing filenames
missing_df = pd.DataFrame({"Missing Filenames": list(missing_filenames)})

# Save to missing_file.csv
missing_df.to_csv(missing_file_csv, index=False)

print(f"Missing filenames saved to {missing_file_csv}")