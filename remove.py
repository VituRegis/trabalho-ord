import os

TAMANHO_CABECALHO = 4
TAMANHO_TAMREGISTRO = 2

def insereNaLED(offset, tamanho):
    ...

def remove(ID_REMOCAO):
    with open('dados.dat','br') as arquivo_dados:
        print(f'\n\nRemoção do registro de chave "{ID_REMOCAO}"')

        TAMANHO_ARQ = arquivo_dados.seek(0, os.SEEK_END)
        
        arquivo_dados.seek(TAMANHO_CABECALHO, os.SEEK_SET)
        
        naoAchou = True
        iterador = 0

        while naoAchou == True:
            iterador += 1
            
            # Pega o tamanho do Registro
            TOTALREG = arquivo_dados.read(TAMANHO_TAMREGISTRO)

            # Pega a posicao inicial do registro antes de ler o ID
            posicao_inicio = arquivo_dados.tell()

            registro = arquivo_dados.read(int.from_bytes(TOTALREG)).decode('utf-8')
            registro_em_lista = registro.split('|')

            if registro_em_lista[0] == ID_REMOCAO:
                print(f'Registro removido! ({int.from_bytes(TOTALREG)} bytes)')
                print(f'Local: offset = {posicao_inicio} bytes ({TOTALREG})')

                insereNaLED(posicao_inicio, int.from_bytes(TOTALREG))

                naoAchou = False

            # Pula para o próximo registro (set na posição onde fica o tamanho do registro anterior e depois pula o valor em bytes)
            arquivo_dados.seek(posicao_inicio, os.SEEK_SET)

            arquivo_dados.seek(int.from_bytes(TOTALREG), os.SEEK_CUR)
            #print(f'Posição do seek depois de pular o registro {arquivo_dados.tell()}')


            if arquivo_dados.tell() >= TAMANHO_ARQ:
                print('Erro: registro não encontrado!')
                naoAchou = False