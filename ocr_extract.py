# ocr_extract.py

import os
from pdf2image import convert_from_path
import pytesseract
from PIL import Image

# Set Tesseract path for Windows
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Path to your PDF
pdf_path = "data/Machine_Learning.pdf"

# Output text file path
output_path = "data/ml_clean_ocr.txt"

# Folder to store temp images
os.makedirs("temp_pages", exist_ok=True)

print("Converting PDF to images...")
images = convert_from_path(pdf_path, dpi=300, output_folder="temp_pages")

text_output = []

print("Running OCR...")
for i, img in enumerate(images):
    text = pytesseract.image_to_string(img)
    text_output.append(f"\n--- Page {i + 1} ---\n{text}")
    print(f"Page {i + 1} processed.")

# Save text to file
with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(text_output))

print(f"OCR complete! Output saved to: {output_path}")
