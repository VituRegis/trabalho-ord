### TRATA OS DADOS PARA NÃO
dados = open('trabalho-ord/dados.dat', 'r').read(-1)
separado = dados[4:-1].split('|')
registros = []
registroAtual = []


### ORGANIZA OS DADOS EM TUPLAS
for i , campo in enumerate(separado):
    campo = str(campo)
    if i % 6 == 0 or i == 599:
        if i != 0 or i == 599:
            registros.append(tuple(registroAtual))

        # ID ESTAVA CORROMPIDO RESOLVI ASSIM:
        if i >= 5994:
            registroAtual = [campo[-4:]]
        elif i >= 594:
            registroAtual = [campo[-3:]]
        elif i >= 54:
            registroAtual = [campo[-2:]]
        elif i >= 0:
            registroAtual = [campo[-1:]]

        registroAtual.append(campo)
        
    else: 
        registroAtual.append(campo)

#for registro in registros:
   # print(registro)

def buscaJogo(identificador):
    achou = False
    for jogos in registros:
        if jogos[0] == identificador:
            print(f'Registro encontrado: {jogos} ({len(((str(jogos[1:]))))- 24} bytes)')
            achou = True
            break

    if achou == False:
        print(f'Registro com identificador [{identificador}] não encontrado!')


def insereJogo(registro):
    print(registro)

def removeJogo(identificador):
    print('removeJogo')

operacoes = open('trabalho-ord/arquivo_operacoes', 'r').readlines(-1)

for operacao in operacoes:
    parametros = operacao[2:-1]

    if operacao[0].lower() == 'b':
        buscaJogo(parametros)

    if operacao[0].lower() == 'i':
        insereJogo(parametros)

    if operacao[0].lower() == 'r':
        removeJogo(parametros)
    
