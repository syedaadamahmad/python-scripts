import os
import csv

def process_directory(root_folder, output_csv):
    unique_files = set()  # To store unique file names
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'sp', 'en', 'also'])

        for foldername, _, filenames in os.walk(root_folder):
            for filename in filenames:
                if filename.endswith("_0.wav"):
                    file_id = os.path.splitext(filename)[0]  # Remove _0.wav extension
                    writer.writerow([file_id, 'noise', 'noise', "[]"])
                    unique_files.add(file_id)

    print(f"Exported {len(unique_files)} unique file names to {output_csv}.")

if __name__ == "__main__":
    target_folder = r"C:\Users\newbr\OneDrive\Desktop\New folder\noise split\noise"
    output_csv_file = "unique_noise.csv"
    process_directory(target_folder, output_csv_file)
