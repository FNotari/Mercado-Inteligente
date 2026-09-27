from rapidocr import RapidOCR

ocr = RapidOCR()

resultado = ocr("teste_cupom.png")

print(resultado)