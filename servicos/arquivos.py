from pathlib import Path

class Arquivos:
    
    def __init__(self, pasta):
        self.pasta = Path(pasta)
        
    def lista_arquivos(self):
        arquivos = self.pasta.glob("*")
        
        return arquivos