from PySide6.QtWidgets import QMainWindow

class JanelaPrincipal(QMainWindow):
   
   def __init__(self):
       super().__init__()
       
       self.setWindowTitle("Mercado Inteligente")
       self.resize(800, 600)