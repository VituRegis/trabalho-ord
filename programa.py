import argparse
import busca
import remove
import insere
import imprime

def imprimeLED():
    imprime.imprime()

def buscaJogo(identificador):
    busca.busca(identificador)

def insereJogo(registro):
    insere.insere(registro)

def removeJogo(identificador):
    remove.remove(identificador)


# Configura o argparse para ler os argumentos da linha de comando
parser = argparse.ArgumentParser(description='Arquivo principal.')

parser.add_argument('-e', dest='arquivo_operacoes', help='Arquivo de operações')
parser.add_argument('-p', action='store_true', help='Executa a função comeCoco')

args = parser.parse_args()

# Verifica se o argumento -p foi passado e imprime a LED
if args.p:
    imprimeLED()
elif args.arquivo_operacoes:
    # Abre e lê o arquivo de operações passado como argumento -e
    try:
        with open(args.arquivo_operacoes, 'r') as file:
            operacoes = file.readlines()

            for operacao in operacoes:
                parametros = operacao[2:-1]

                if operacao[0].lower() == 'b':
                    buscaJogo(parametros)

                elif operacao[0].lower() == 'i':
                    insereJogo(parametros)

                elif operacao[0].lower() == 'r':
                    removeJogo(parametros)
                else:
                    print(f"Operação desconhecida: {operacao[0]}")
    except FileNotFoundError:
        print(f"Arquivo {args.arquivo_operacoes} não encontrado.")
else:
    print("\n Nenhum argumento válido foi passado.\n Use 'python programa.py -e arquivo_operacoes' para rodar o arquivo de operações ou 'python programa.py -p' para imprimir a LED.\n")

busca.arquivo_dados.close()
insere.arquivo_dados.close()
remove.arquivo_dados.close()
imprime.arquivo_dados.close()