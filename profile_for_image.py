import os
import pandas as pd
from PIL import Image

# Function to extract features from an image
def extract_features(image_path):
    img = Image.open(image_path)
    width, height = img.size
    # Other feature extraction logic can be added here
    return {'Image_Path': image_path, 'Width': width, 'Height': height}

# Directory containing images
image_dir = 'path_to_your_image_directory'

# List to hold extracted features
image_data = []

# Iterate over each image in the directory
for filename in os.listdir(image_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(image_dir, filename)
        features = extract_features(image_path)
        image_data.append(features)

# Create DataFrame from the extracted features
image_df = pd.DataFrame(image_data)

# Now you can use pandas profiling on image_df
from pandas_profiling import ProfileReport

profile = ProfileReport(image_df, title="Pandas Profiling Report")
profile.to_file("image_profile_report.html")
