import os
import subprocess

# Define the path to the labeling folder
labeling_folder = 'workspace/images/collected_images'

# Ensure the labeling folder exists
if not os.path.exists(labeling_folder):
    print(f"Labeling folder '{labeling_folder}' does not exist. Please collect images first.")
    exit(1)

# Launch labelImg for labeling
try:
    subprocess.run(['labelImg', labeling_folder], check=True)
except FileNotFoundError:
    print("labelImg is not installed or not found in PATH. Please ensure it is installed and accessible.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while running labelImg: {e}")