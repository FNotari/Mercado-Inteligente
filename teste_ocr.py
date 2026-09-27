import pytesseract
from PIL import Image

imagem = Image.open("teste_cupom.png")

texto = pytesseract.image_to_string(imagem, lang="por")

print(texto)