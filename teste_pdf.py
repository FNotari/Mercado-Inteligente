import pymupdf

arquivo = "F:/Mercado-Inteligente/cupons/IMG_20260816_0001.pdf"

documento = pymupdf.open(arquivo)

pagina = documento[0]

pix = pagina.get_pixmap()

pix.save("teste_cupom.png")

documento.close()

print("Imagem criada")