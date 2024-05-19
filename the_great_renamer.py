import os
import re

# Define a function to insert spaces before capital letters
def add_spaces(name):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", name)

# Get the path of the 'all_audio' directory
dir_path = 'all_audio'

# Get the list of subdirectories in the 'all_audio' directory
subdirectories = next(os.walk(dir_path))[1]

# Apply the function to the names of the subdirectories and rename them
for name in subdirectories:
    new_name = add_spaces(name)
    os.rename(os.path.join(dir_path, name), os.path.join(dir_path, new_name))