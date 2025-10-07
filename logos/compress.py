import os
from PIL import Image

def compress_image(input_path, output_path, max_size_kb=300):
    img = Image.open(input_path)
    img_format = img.format
    quality = 95
    step = 5

    # Try reducing quality until under max_size_kb
    while True:
        img.save(output_path, format=img_format, quality=quality, optimize=True)
        size_kb = os.path.getsize(output_path) / 1024
        if size_kb <= max_size_kb or quality <= 10:
            break
        quality -= step

logos_dir = "logos"
for filename in os.listdir(logos_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(logos_dir, filename)
        output_path = input_path  # Overwrite original
        compress_image(input_path, output_path)
        print(f"Compressed {filename}")

print("Compression complete.")