import os
import shutil

# Source and destination directories
source_dir = r"C:\arabic 4.0\Extracted\Client"
dest_dir = r"C:\Users\al5ya\OneDrive\Documents\GitHub\Texts_AR\Extracted\Clients"

# Walk through the source directory
for root, _, files in os.walk(source_dir):
    # Generate the corresponding path in the destination directory
    dest_root = root.replace(source_dir, dest_dir, 1)
    
    # Ensure the corresponding destination directory exists
    os.makedirs(dest_root, exist_ok=True)
    
    # Copy .txt files from source to destination
    for file in files:
        if file.endswith(".txt"):
            source_file = os.path.join(root, file)
            dest_file = os.path.join(dest_root, file)
            try:
                shutil.copy2(source_file, dest_file)
                print(f"Copied: {source_file} to {dest_file}")
            except Exception as e:
                print(f"Error copying {source_file} to {dest_file}: {e}")
            
print("Copying .txt files completed.")
