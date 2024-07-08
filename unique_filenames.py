import os
import csv

def get_species(subfolder_name):
    if subfolder_name == "Blue-cappedRockThrush":
        return "Monticola cinclorhyncha"
    elif subfolder_name == "PlainMountainFinch":
        return "Leucosticte nemoricola"
    elif subfolder_name == "CommonRosefinch":
        return "Carpodacus erythrinus"
    else:
        return ""

def process_directory(root_folder, output_csv):
    unique_files = set()  # To store unique file names
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'sp', 'en', 'also'])

        for foldername, _, filenames in os.walk(root_folder):
            subfolder_name = os.path.basename(foldername)
            species = get_species(subfolder_name)

            for filename in filenames:
                file_id = os.path.splitext(filename)[0]  # Remove file extension
                writer.writerow([file_id, species, subfolder_name, "[]"])
                unique_files.add(file_id)

    print(f"Exported {len(unique_files)} unique file names to {output_csv}.")

if __name__ == "__main__":
    target_folder = r"C:\Users\newbr\OneDrive\Desktop\New folder\Remainder_names_fixed_total_SCI_UPDATED"
    output_csv_file = "unique.csv"
    process_directory(target_folder, output_csv_file)