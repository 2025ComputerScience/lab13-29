!sudo apt update
!sudo apt install tesseract-ocr tesseract-ocr-chi-tra

!pip install pytesseract

from google.colab import files
uploaded = files.upload()

from PIL import Image, ImageOps
import pytesseract
import matplotlib.pyplot as plt

#取得使用者上傳的檔案名稱(只上傳一個)
filename = list(uploaded.keys())[0]

image = Image.open(filename)

#顯示上傳的圖片，確認是否成功讀取
plt.imshow(image)
plt.axis('off')

#同時辨識繁體中文與英文
text = pytesseract.image_to_string(image, lang='chi_tra+eng', config='--psm 6')

print("OCR 辨識結果:")
print("-" * 40)
print(text)
