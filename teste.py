from servicos.configuracoes import Configuracoes

config = Configuracoes()

config.tema = "claro"
config.pasta_cupons = "D/Mercado"
config.primeira_execucao = False
config.salvar()


print(config.tema)
print(config.pasta_cupons)
print(config.primeira_execucao)