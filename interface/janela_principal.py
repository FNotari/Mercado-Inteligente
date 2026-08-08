from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog

class JanelaPrincipal(QMainWindow):
   
   def __init__(self, configuracoes):
       super().__init__()
       
       self.configuracoes = configuracoes
       
       #Criando a janela com o título
       self.setWindowTitle("Mercado Inteligente")
       self.resize(800, 600)
       
       #Criando o widget
        #Criando o Texto
       self.texto = QLabel("Bem-vindo ao Mercado Inteligente")
       
        #Criando o botão
       self.botao = QPushButton("Escolher pasta")
       
        #Criando o Layout
       layout = QVBoxLayout()
       
        #Adicionando os widgets ao layout
       layout.addWidget(self.texto)
       layout.addWidget(self.botao)
       
       #Criando o widget central
       widget_central = QWidget()
       
       #Coloando o layout e o widget dentro da janela
       widget_central.setLayout(layout)
       self.setCentralWidget(widget_central)
       
       #Fazendo a conecxão do botão
       self.botao.clicked.connect(self.escolher_pasta)
   
   #Quando clicar no botão, o usuário deverá escolher uma pasta    
   def escolher_pasta(self):
        print("Botão clicado")
        
        pasta = QFileDialog.getExistingDirectory(self, "Selecionar pasta")
        
        if pasta:
            print(pasta)
            self.configuracoes.pasta_cupons = pasta
            self.configuracoes.salvar()
            return pasta
        else:
            print("Pasta não selecionada")
            return None