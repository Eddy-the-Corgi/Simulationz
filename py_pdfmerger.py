from PIL import Image
import os

input_folder = "/home/kre/u/s/s/50"
output_pdf = "merged_screenshots2.pdf"

image_files = sorted([
    os.path.join(input_folder, f)
    for f in os.listdir(input_folder)
    if f.endswith(".png")
])

images = [Image.open(f).convert("RGB") for f in image_files]

if images:
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"PDF saved as {output_pdf}")
else:
    print("No PNG files found!")