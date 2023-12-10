import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
def contenuText(chemin):
    text=""
    for ch in chemin :
        img = Image.open(ch)
        text = text + tess.image_to_string(img)+"."
    return text