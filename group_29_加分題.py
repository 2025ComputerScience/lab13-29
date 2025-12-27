!sudo apt update
!sudo apt install tesseract-ocr tesseract-ocr-chi-tra

!pip install pytesseract

from google.colab import files
uploaded = files.upload()

from PIL import Image, ImageOps
import pytesseract
import matplotlib.pyplot as plt

filename = list(uploaded.keys())[0]

image = Image.open(filename)

plt.imshow(image)
plt.axis('off')

text = pytesseract.image_to_string(image, lang='chi_tra+eng', config='--psm 6')

print("OCR 辨識結果:")
print("-" * 40)
print(text)
