from interface.janela_principal import JanelaPrincipal
from servicos.configuracoes import Configuracoes
from PySide6.QtWidgets import QApplication

def main():
    configuracoes = Configuracoes()
    
    app = QApplication([])
    janela = JanelaPrincipal()
    janela.show()
    app.exec()
    
    print("Progrma iniciado")
    print(configuracoes.tema)
    
if __name__ == "__main__":
        main()
        

    