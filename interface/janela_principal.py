from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class JanelaPrincipal(QMainWindow):
   
   def __init__(self):
       super().__init__()
       
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
       
       #Fazendo o botão funcionar
       self.botao.clicked.connect(self.escolher_pasta)
       
   def escolher_pasta(self):
        print("Botão clicado")