import cv2

arquivo = "F:\Mercado-Inteligente\cupons\qr.jpg"

imagem = cv2.imread(arquivo)

if imagem is None:
    print("Imagem não foi encontrada")
    exit()
    
altura, largura = imagem.shape[:2]

print("Largura:", largura)
print("Altura:", altura)

recorte = imagem[int(altura * 0.20):int(altura * 0.75), int(largura * 0.10):int(largura * 0.90)]

cv2.imwrite("recorte_qrcode.jpg", recorte)

print("Recorte criado com sucesso")    