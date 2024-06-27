#This script reads the CSV file, identifies matching filenames, and moves the corresponding files from the audio directory to the new folder “H_list_89.”

import os
import shutil

# Define source and destination directories
source_dir = r"C:\Users\newbr\OneDrive\Desktop\New folder"
destination_dir = r"D:\B_model_code\H_list_89"
audio_dir = r"D:\B_model_code\all_audio_split_314"

# Read the CSV file
csv_file = os.path.join(source_dir, "list_en_ml.csv")
if not os.path.exists(csv_file):
    print(f"CSV file '{csv_file}' not found.")
else:
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Read the CSV and move files
    with open(csv_file, "r") as f:
        next(f)  # Skip the header
        for line in f:
            filename = line.strip()  # Remove leading/trailing spaces
            source_path = os.path.join(audio_dir, filename)
            destination_path = os.path.join(destination_dir, filename)
            if os.path.exists(source_path):
                shutil.move(source_path, destination_path)
                print(f"Moved '{filename}' to '{destination_dir}'")
            else:
                print(f"File '{filename}' not found in '{audio_dir}'")