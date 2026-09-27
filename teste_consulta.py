import requests
from bs4 import BeautifulSoup

url = "http://www.dfe.ms.gov.br/nfce/qrcode?p=50260984683481061478650010002940871776842553|2|1|1|D922F199799B6EBF72D58A0109560C9069F33227"

resposta = requests.get(url)

soup = BeautifulSoup(resposta.text, "html.parser")

produto = soup.find("span", class_="txtTil")

if produto:
    print("Produto encontrado:")
    print(produto.get_text(strip=True))
else:
    print("Produto não encontrado")    
    
"""print("Status:", resposta.status_code)
print("Tamnho da resposta:", len(resposta.text))

print(resposta.text[:1000])

palavras = ["Produto","Quantidade","Valor unitário", "Valor total"]

for palavra in palavras:
    if palavra in resposta.text:
        print("Encontrou:", palavra)
    else:
        print("Não encontrou:",palavra)    
        
posicao = resposta.text.find("Valor total")

if posicao != -1:
    print("\n Trecho encontrado")
    print(resposta.text[posicao - 1000:posicao + 2000])"""