import pandas as pd

# Read the list_sp_ml.csv and paper.csv files
list_sp_ml_path = r'C:\Users\newbr\OneDrive\Desktop\B_model_87\inputs\list_sp_ml.csv'
paper_path = r'C:\Users\newbr\OneDrive\Desktop\B_model_87\paper.csv'

list_sp_ml_df = pd.read_csv(list_sp_ml_path)
paper_df = pd.read_csv(paper_path)

# Get unique species names from both dataframes
sp_ml_names = set(list_sp_ml_df['sp'])
paper_names = set(paper_df['sp'])

# Find names absent in either dataframe
absent_names = sp_ml_names.symmetric_difference(paper_names)

# Create a DataFrame with columns "Scientific name" and "File from which name is absent"
absent_df = pd.DataFrame({'Scientific name': list(absent_names), 'File from which name is absent': ''})

# Mark the source file for each absent name
for name in absent_names:
    if name in sp_ml_names:
        absent_df.loc[absent_df['Scientific name'] == name, 'File from which name is absent'] = 'list_sp_ml.csv'
    if name in paper_names:
        absent_df.loc[absent_df['Scientific name'] == name, 'File from which name is absent'] = 'paper.csv'

# Save absent names to a new CSV file
absent_df.to_csv('names_absent.csv', index=False)

print("Absent names saved to names_absent.csv")