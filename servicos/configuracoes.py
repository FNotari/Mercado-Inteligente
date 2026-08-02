import json
from pathlib import Path

class Configuracoes:
    def __init__(self):
        self.arquivo_configuracoes = Path("dados/config.json")
        
        self.pasta_cupons = ""
        self.tema = "claro"
        self.primeira_execucao = True
        self.carregar()
        
        
    def carregar(self):
        if not self.arquivo_configuracoes.exists():
            return
        
        #Abrir o config.json e ler e fechar
        with open(self.arquivo_configuracoes, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            self.tema = dados["tema"]
            self.pasta_cupons = dados["pasta_cupons"]
            self.primeira_execucao = dados["primeira_execucao"]
            
    def salvar(self):
        with open(self.arquivo_configuracoes, "w", encoding="utf-8") as arquivo:
            dados = {"tema": self.tema, "pasta_cupons": self.pasta_cupons, "primeira_execucao": self.primeira_execucao}
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            