### TRATA OS DADOS PARA NÃO
dados = open('trabalho-ord/dados.dat', 'r').read(-1)
separado = dados[4:-1].split('\x00')

for i, registros in enumerate(separado):
    print(registros[i])
