from PIL import Image
import sys
import os

def compress_image(input_path, output_path, max_size_kb=300):
    img = Image.open(input_path)
    quality = 95
    img_format = img.format if img.format else "JPEG"

    # Try reducing quality until under max_size_kb
    while quality > 10:
        img.save(output_path, format=img_format, quality=quality, optimize=True)
        size_kb = os.path.getsize(output_path) / 1024
        if size_kb <= max_size_kb:
            print(f"Compressed to {size_kb:.2f} KB at quality={quality}")
            return
        quality -= 5

    print("Could not compress under target size with acceptable quality.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compressed.py <input_image> <output_image>")
        sys.exit(1)
    compress_image(sys.argv[1], sys.argv[2])