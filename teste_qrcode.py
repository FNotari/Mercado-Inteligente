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

cinza = cv2.cvtColor(recorte, cv2.COLOR_BGR2GRAY)

resultado = cv2.threshold( cinza, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

preto_branco = resultado[1]

cv2.imwrite("qr_preto_branco.jpg", preto_branco)

print("Recorte criado com sucesso") 

leitor = cv2.QRCodeDetector()

dados, pontos, _ = leitor.detectAndDecode(preto_branco)

if dados:
    print("QR encontrado")
    print(dados)
else:
    print("A imagem foi aberta, mas o QR code não foi lido")
    
 
"""print("Imagem carregada com sucesso")
print("Largura:", imagem.shape[1])
print("Altura:", imagem.shape[0])    

leitor = cv2.QRCodeDetector()

dados, pontos, _ = leitor.detectAndDecode(imagem)

if dados:
    print("QR encontrado")
    print(dados)
else:
    print("A imagem foi aberta, mas o QR code não foi lido")"""   