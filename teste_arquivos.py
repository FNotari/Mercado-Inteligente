from servicos.arquivos import Arquivos

arquivos = Arquivos("F:/Mercado-Inteligente/cupons")
lista = arquivos.listar_cupons()

for arquivo in lista:
    print(arquivo)