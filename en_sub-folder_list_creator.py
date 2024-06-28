import os
import csv

def save_subfolder_names_to_csv(folder_path):
    # Get a list of sub-folder names
    subfolders = [subfolder for subfolder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, subfolder))]

    # Create a CSV file and write sub-folder names
    csv_file = os.path.join(folder_path, "list_en_ml.csv")
    with open(csv_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["subfolder_name"])  # Write header
        for subfolder in subfolders:
            writer.writerow([subfolder])

    print(f"Sub-folder names saved to {csv_file}")

# Specify the folder path
folder_path = r"D:\B_model_code\H_list_87"

# Call the function
save_subfolder_names_to_csv(folder_path)
