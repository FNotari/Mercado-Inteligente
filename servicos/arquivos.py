from pathlib import Path

class Arquivos:
    #Inicia a classe mostrando para ela onde esta a pasta de cupons
    def __init__(self, pasta):
        self.pasta = Path(pasta)
    
    #Cria uma lista de todos os arquivos que contém na pasta    
    def listar_arquivos(self):
        arquivos = self.pasta.glob("*")
        return list(arquivos)
    
    #Cria um filtro para os formatos pdf, jpg, jpeg e png
    def listar_cupons(self):
        arquivos = self.listar_arquivos()
        
        extensoes_permitidas = [".pdf", ".jpg", ".jpeg", ".png"]
        
        cupons = []
        
        for arquivo in arquivos:
            if arquivo.suffix.lower() in extensoes_permitidas:
                cupons.append(arquivo)
                
        return cupons        