from interface.janela_principal import JanelaPrincipal
from servicos.configuracoes import Configuracoes
from PySide6.QtWidgets import QApplication

def main():
    configuracoes = Configuracoes()
    
    app = QApplication([])
    janela = JanelaPrincipal(configuracoes)
    janela.show()
    print("Programa iniciado")
    print(configuracoes.tema)    
    app.exec()
        
if __name__ == "__main__":
        main()
        

    