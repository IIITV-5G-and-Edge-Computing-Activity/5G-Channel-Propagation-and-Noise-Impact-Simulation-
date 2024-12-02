from PIL import Image
import os

# Define the desired dimensions
new_size = (400, 300)

# Directory containing images
image_dir = "./Analysis"

for image_name in os.listdir(image_dir):
    if image_name.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(image_dir, image_name)
        img = Image.open(image_path)
        img_resized = img.resize(new_size)
        img_resized.save(image_path)  # Overwrite the original file
